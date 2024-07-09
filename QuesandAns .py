#Q&A

import spacy
from transformers import pipeline
nlp = spacy.load("en_core_web_sm")
qa_pipeline = pipeline("question-answering")
paragraph = input("Please enter the paragraph: ")
doc = nlp(paragraph)
print("\nNamed Entities, spans, and labels:")
for ent in doc.ents:
    print(f"{ent.text} ({ent.start_char}, {ent.end_char}): {ent.label_}")
def answer_question(question, context):
    result = qa_pipeline(question=question, context=context)
    return result["answer"]
print("\nAsk your questions (type 'exit' to stop):")
while True:
    question = input("Question: ")
    if question.lower() == 'exit':
        break
    answer = answer_question(question, paragraph)
    print(f"Answer: {answer}\n")

#paragraphs used

#PARA 1
"""Barack Obama was born on August 4, 1961, in Honolulu, Hawaii.
He served as the 44th President of the United States from 2009 to 2017. 
He is a member of the Democratic Party, and he was the first African American to hold the office.
Michelle Obama, his wife, was the First Lady of the United States during his presidency."""

#PARA-2
"""Plant-eating dinosaurs had teeth of various shapes designed for their particular diets. 
Triceratops, for example, had hundreds of teeth that formed a solid “wall” with sharp ridges. 
The teeth were used to chop off vegetation. Other plant eaters, such as Anatotitan, 
had wide flat teeth that they used to grind up tough vegetation. The long-necked dinosaurs, such as Diplodocus, 
had long pencil-like teeth that they used to rake the leaves off branches. These dinosaurs swallowed the leaves whole. They also ingested small stones, called gastroliths,
most likely to grind up the food in their stomachs, much the same way modern birds, such as parakeets and chickens, do today."""

#PARA 3
"""Python is used for server-side web development, software development, mathematics, and system scripting, and is popular for Rapid Application Development and as a scripting or glue language to tie existing components because of its high-level, 
built-in data structures, dynamic typing, and dynamic binding. 
Program maintenance costs are reduced with Python due to the easily learned syntax and emphasis on readability. 
Additionally, Python's support of modules and packages facilitates modular programs and reuse of code.
Python is an open source community language, so numerous independent programmers are continually building libraries and functionality for it."""

#PARA 4
"""The enigmatic conference held in Zurich in October 2022, which, according to the obscure schedule distributed by the organizing committee, aimed to explore the intersection of quantum computing and ancient philosophy, attracted a diverse group of attendees ranging from theoretical physicists to historians of ancient civilizations.
During the keynote speech, Dr. Alexei Voronov, who had previously collaborated with the CERN team on Higgs boson experiments, presented an intricate theory suggesting that Plato's allegory of the cave was an early conceptualization of quantum entanglement. 
This controversial hypothesis, although dismissed by many as a mere academic curiosity, received unexpected support from Professor Amelia Rodriguez of the University of Salamanca, who argued that ancient texts often contain insights that resonate with modern scientific discoveries.
However, the sudden announcement of a previously unscheduled panel featuring a heated debate between proponents of string theory and advocates of loop quantum gravity added another layer of complexity to the already convoluted discussions. Adding to the confusion, the panel's moderator, an AI developed by the MIT Media Lab, malfunctioned mid-session, leading to a chaotic exchange that left many participants bewildered.
The aftermath of the conference saw a flurry of publications, both supportive and critical, attempting to decipher the implications of the discussions, with some claiming that the event marked a new era of interdisciplinary research, while others dismissed it as an intellectually stimulating but ultimately inconsequential gathering."""