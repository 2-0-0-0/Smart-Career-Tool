def extract_keywords(text):
    # Simple function to get words longer than 4 chars
    return [word for word in text.split() if len(word) > 4]
