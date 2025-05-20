import streamlit as st
import os
from dotenv import load_dotenv
from datasets import load_dataset

load_dotenv()

st.set_page_config(
    page_title="Court Rulings (COI)",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="expanded",
)

if "document_topic_data" not in st.session_state:
    with st.spinner("Loading dataset..."):
        # Load the dataset
        st.session_state.document_topic_data = load_dataset(
            "francescoortame/court-rulings-document-topic", split="train"
        )

st.text_input("Cosa stai cercando?", key="search_query")