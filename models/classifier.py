from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

training_data = [
    ("meeting project deadline", "Work"),
    ("family dinner tonight", "Personal"),
    ("win money now click here", "Spam"),
    ("submit assignment today", "Important")
]

texts = [t[0] for t in training_data]
labels = [t[1] for t in training_data]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

def classify_email(text):
    test = vectorizer.transform([text])
    return model.predict(test)[0]
