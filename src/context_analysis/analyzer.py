import spacy

nlp = spacy.load("en_core_web_sm")

def analyze_text(text):
    doc = nlp(text)
    return {
        "tone": "formal" if any(token.pos_ == "ADJ" for token in doc) else "informal",
        "topics": [ent.text for ent in doc.ents]
    }
