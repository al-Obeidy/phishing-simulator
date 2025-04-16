from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

vectorizer = CountVectorizer()
classifier = LogisticRegression()

def evaluate_message(message):
    vector = vectorizer.transform([message])
    prediction = classifier.predict(vector)
    return "Phishing" if prediction == 1 else "Not Phishing"
