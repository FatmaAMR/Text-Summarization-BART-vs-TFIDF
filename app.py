import streamlit as st
import requests

st.set_page_config(page_title="Sentinel AI | Benchmarking", layout="wide")

# Custom Professional Theme
st.markdown('''
    <style>
    .stApp { background-color: #F4F7F9; }
    .compare-card {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 8px;
        border-left: 5px solid #1E3A8A;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        min-height: 350px;
        color: #334155;
        font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
    }
    .title-text { 
        color: #1E3A8A; 
        font-weight: 700; 
        letter-spacing: -0.5px;
        margin-bottom: 5px;
    }
    .sub-title { color: #64748B; margin-bottom: 30px; font-size: 18px; }
    h3 { color: #1E3A8A !important; font-size: 20px !important; margin-bottom: 15px !important; }
    
    .stButton>button {
        background-color: #1E3A8A;
        color: white;
        border-radius: 4px;
        border: none;
        padding: 10px 24px;
        font-weight: 600;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #111827;
        color: #FFFFFF;
        border: none;
    }
    </style>
    ''', unsafe_allow_html=True)

st.markdown('<h1 class="title-text">Sentinel AI: Summarization Comparison</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Extractive (Baseline) vs. Abstractive (Advanced) Performance Analysis</p>', unsafe_allow_html=True)

source_text = st.text_area("Source Article / Input Document", height=250, placeholder="Paste your text content here...")

if st.button("Generate Comparison Analysis"):
    if source_text:
        with st.spinner("Analyzing document structure..."):
            try:
                # API Call to local backend
                res = requests.post("http://127.0.0.1:8000/compare", json={"text": source_text}, timeout=120)
                data = res.json()
                
                col_l, col_r = st.columns(2)
                with col_l:
                    st.markdown("<h3>Baseline Model Summary</h3>", unsafe_allow_html=True)
                    st.markdown(f'<div class="compare-card">{data["baseline"]}</div>', unsafe_allow_html=True)
                    st.caption("Algorithm: Statistical TF-IDF Ranking")
                    
                with col_r:
                    st.markdown("<h3>Advanced Model Summary</h3>", unsafe_allow_html=True)
                    st.markdown(f'<div class="compare-card">{data["advanced"]}</div>', unsafe_allow_html=True)
                    st.caption("Model: Transformer-based Seq2Seq (BART)")
            except Exception as e:
                st.error(f"Connection Error: Ensure the Backend (main.py) is running. Details: {e}")
    else:
        st.warning("Please enter source text to proceed.")