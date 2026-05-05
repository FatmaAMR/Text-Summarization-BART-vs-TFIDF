# AI Summarization: Comparative Analysis System

This repository hosts a professional system designed to evaluate and compare two different methodologies for text summarization: **Extractive** (Statistical) and **Abstractive** (Generative). The goal is to analyze the trade-offs between computational efficiency and linguistic coherence.

## System Architecture
The project follows a decoupled client-server architecture:
- **Backend (FastAPI):** Handles intensive model inference and text processing logic.
- **Frontend (Streamlit):** Provides a high-contrast, professional interface for real-time analysis.

## Comparison Methodologies
1. **Extractive Summarization (Baseline):** Uses TF-IDF vectorization to rank sentences based on statistical importance. This method is highly efficient and ensures factual consistency by selecting original text segments.
2. **Abstractive Summarization (Advanced):** Utilizes a fine-tuned BART (Bidirectional and Auto-Regressive Transformers) model. It generates new sentences to capture the essence of the text, providing a more human-like summary.

---

## Local Directory Structure
Ensure your local environment is organized as follows:
```text
summarization-analysis/
├── Advanced_Model/     # Local folder for BART transformer weights
├── Baseline_Model/     # Local folder for the TF-IDF vectorizer
├── config.py           # Path configuration management
├── main.py             # FastAPI backend implementation
├── app.py              # Streamlit professional UI
└── requirements.txt    # Project dependencies
```


## Setup and Installation

1. Clone the Repository

```bash
git clone [https://github.com/FatmaAMR/Text-Summarization-BART-vs-TFIDF.git](https://github.com/FatmaAMR/Text-Summarization-BART-vs-TFIDF.git)
cd summarization-analysis
```
2. Environment Setup
Install all required libraries using pip:

```bash
pip install -r requirements.txt
```

3. Model Acquisition

The `Advanced_Model` directory containing the transformer weights must be downloaded separately due to its size (approx. 1.2GB).

    ```bash
    Download Link: [model.safetensors](https://drive.google.com/file/d/1wTPqTgkIrfL9g7SYPUOQl6JDeC_g8VeJ/view?usp=sharing)
    ```

    Placement: Move the downloaded folder into the project root directory.



## Operating Instructions

The system requires two active terminal sessions to function:

**Terminal 1: API Backend**
Launches the FastAPI server to handle model requests.
```bash
python main.py
```

**Terminal 2: Web Interface**
Launches the professional dashboard in your browser.
```bash
streamlit run app.py
```