import re
from nltk.tokenize import word_tokenize


def clean_text(text):
    # Remove special characters and extra whitespace
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    cleaned_text = ' '.join(cleaned_text.split())
    return cleaned_text


def tokenize_text(text):
    return word_tokenize(text)

from nltk.stem import WordNetLemmatizer

def lemmatize_text(tokens):
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return lemmatized_tokens
