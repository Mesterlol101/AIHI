# task 4-1
import spacy
# Define included_entities
include_entities = ['DATE', 'ORG', 'PERSON']
nlp = spacy.load('en_core_web_md')

# Define extract_entities()
def extract_entities(message):
    # Create a dict to hold the entities
    ents = {}
    # Create a spacy document
    doc = nlp(message)
    for ent in doc.ents:
        if ent.label_ in include_entities:
            # Save interesting entities
            ents[ent.label_] = ent.text
    return ents

print(extract_entities('friends called Janet who have worked at Google since 2010'))
print(extract_entities('people who graduated from MIT in 1999'))
