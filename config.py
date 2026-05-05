import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

VECTORIZER_PATH = os.path.join(BASE_DIR, "Baseline_Model", "tfidf_vectorizer.pkl")
TRANSFORMER_PATH = os.path.join(BASE_DIR, "Advanced_Model")