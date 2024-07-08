import requests
from spacy.lang.en import English
from spacy.language import Language
from spacy.matcher import PhraseMatcher
from spacy.tokens import Doc, Span

@Language.factory("rest_countries")
class RESTCountriesComponent:
    def __init__(self, nlp, name, label="GPE"):
        self.label = label
        self.matcher = PhraseMatcher(nlp.vocab)
        self.countries = self.load_countries()

        # Register extensions on Span for storing country attributes
        Span.set_extension("is_country", default=False)
        Span.set_extension("country_capital", default=None)
        Span.set_extension("country_latlng", default=None)
        Span.set_extension("country_flag", default=None)

        # Add country names to matcher
        patterns = [nlp.make_doc(country) for country in self.countries.keys()]
        self.matcher.add("COUNTRIES", None, *patterns)

    def __call__(self, doc):
        matches = self.matcher(doc)
        spans = []
        for _, start, end in matches:
            country_name = doc[start:end].text
            country_data = self.countries[country_name]
            span = Span(doc, start, end, label=self.label)
            span._.is_country = True
            span._.country_capital = country_data.get("capital")
            span._.country_latlng = country_data.get("latlng")
            span._.country_flag = country_data.get("flag")
            spans.append(span)
        doc.ents = list(doc.ents) + spans
        return doc

    def load_countries(self):
        try:
            r = requests.get("https://restcountries.com/v2/all")
            r.raise_for_status()
            countries = {c["name"]: c for c in r.json()}
            return countries
        except requests.exceptions.RequestException as e:
            print(f"Error loading countries: {e}")
            return {}

    @property
    def has_country(self):
        return any([ent._.is_country for ent in doc.ents])

# Example usage
nlp = English()
nlp.add_pipe("rest_countries", config={"label": "GPE"})
doc = nlp("Some text about Colombia and the Czech Republic")
print("Pipeline:", nlp.pipe_names)
print("Doc has countries:", doc._.has_country)

for ent in doc.ents:
    if ent._.is_country:
        print(ent.text, ent.label_, ent._.country_capital, ent._.country_latlng, ent._.country_flag)
