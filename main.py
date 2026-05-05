from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from nltk.tokenize import sent_tokenize
import config
import nltk
import uvicorn
import sys

# Download required NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')

app = FastAPI()

# Global model loading
try:
    device = "cuda" if torch.cuda.is_available() else "cpu"
    # Load TF-IDF components
    vectorizer = joblib.load(config.VECTORIZER_PATH)
    # Load Transformer components
    tokenizer = AutoTokenizer.from_pretrained(config.TRANSFORMER_PATH)
    model = AutoModelForSeq2SeqLM.from_pretrained(config.TRANSFORMER_PATH).to(device)
    print(f"Server Status: Models loaded successfully on {device}")
except Exception as e:
    print(f"Configuration Error: {e}")
    sys.exit(1)

class SummaryRequest(BaseModel):
    text: str

@app.post("/compare")
async def compare(request: SummaryRequest):
    try:
        # Execution: Baseline Summary (Extractive)
        sentences = sent_tokenize(request.text)
        matrix = vectorizer.transform(sentences)
        scores = matrix.sum(axis=1).flatten().tolist()[0]
        ranked = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
        baseline_res = " ".join([ranked[i][1] for i in range(min(3, len(sentences)))])
        
        # Execution: Advanced Summary (Abstractive)
        inputs = tokenizer(request.text, max_length=1024, return_tensors="pt", truncation=True).to(device)
        output_ids = model.generate(inputs["input_ids"], max_length=150, min_length=40, num_beams=4)
        advanced_res = tokenizer.decode(output_ids[0], skip_special_tokens=True)
        
        return {"baseline": baseline_res, "advanced": advanced_res}
    except Exception as e:
        return {"baseline": "Error", "advanced": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)