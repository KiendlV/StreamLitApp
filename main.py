import streamlit as st
from page_utilites import get_favicon

st.set_page_config(
        page_title="MLAAS",
        page_icon=get_favicon()
)

st.title("Machine Learning Hub")

st.sidebar.title("Navigation")

st.sidebar.file_uploader("Upload a file")

st.write("OpenAI: GPT Connector")

