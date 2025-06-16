import nltk
import numpy as np
import pandas as pd
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def load_faqs(filename="faqs.csv"):
    # Read the CSV with proper quoting and space handling
    df = pd.read_csv(filename, quotechar='"', skipinitialspace=True)
    return dict(zip(df['Question'], df['Answer']))

def preprocess(text):
    # Lowercase
    text = text.lower()
    # Remove non-alphanumeric characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # Tokenize
    tokens = word_tokenize(text)
    # Remove stopwords and punctuation
    tokens = [word for word in tokens if word not in stopwords.words('english') and word not in string.punctuation]
    return ' '.join(tokens)

# Load FAQs
faqs = load_faqs()
questions = list(faqs.keys())
answers = list(faqs.values())

# Preprocess questions
preprocessed_questions = [preprocess(q) for q in questions]

# Vectorize
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(preprocessed_questions)

def get_response(user_input):
    user_input_processed = preprocess(user_input)
    user_vec = vectorizer.transform([user_input_processed])
    similarities = cosine_similarity(user_vec, X)
    idx = np.argmax(similarities)

    if similarities[0][idx] > 0.2:
        return answers[idx]
    else:
        return "I'm sorry, I don't have an answer for that."
