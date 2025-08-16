def extract_keywords(text):
    return [word for word in text.split() if len(word) > 4]

