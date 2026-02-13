urgent_keywords = ["urgent", "asap", "immediately", "deadline", "important"]

def detect_priority(text):
    text = text.lower()

    for word in urgent_keywords:
        if word in text:
            return "High"

    if len(text) > 100:
        return "Medium"

    return "Low"
