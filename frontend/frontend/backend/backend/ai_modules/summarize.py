def summarize(text):
    sentences = text.split('.')
    return '. '.join(sentences[:2]) + '.' if len(sentences)>1 else text
