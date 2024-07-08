#hints & validations

import spacy
from spacy.language import Language
from spacy.tokens import Doc
from pydantic import StrictStr
import logging

@spacy.component("debug", factory=True)
class DebugComponent:
    def __init__(self, nlp: Language, name: str, log_level: StrictStr):
        self.logger = logging.getLogger(f"spacy.{name}")
        self.logger.setLevel(log_level)
        self.logger.info(f"Pipeline: {nlp.pipe_names}")

    def __call__(self, doc: Doc) -> Doc:
        is_tagged = doc.has_annotation("TAG")
        self.logger.debug(f"Doc: {len(doc)} tokens, is tagged: {is_tagged}")
        return doc
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("debug", config={"log_level": "DEBUG"})
doc = nlp("This is a sample text...")
print(doc)
