def summarize_email(text):
    sentences = text.split(".")
    return ".".join(sentences[:2])
