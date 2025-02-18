import streamlit as st

st.title("ML Model Financial Tracker")

st.write("Please Upload a CSV of your financials")

uploaded_file = st.file_uploader("Choose a file")
