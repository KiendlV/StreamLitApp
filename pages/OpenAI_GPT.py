import streamlit as st
from GPT import gpt_connector

st.title("GPT Connector")

st.write("This is a connector to the OpenAI GPT Model. Prompt anything you need to know.")

conn = gpt_connector.OpenAIConn()

if "gpt_output" not in st.session_state:
    st.session_state.gpt_output = ""

user_input = st.text_area("What can i do for you:")

st.write(f"Question: {user_input}")

#st.button("Ask", on_click=conn.get_feedback)
st.write(f"Answer: {st.session_state.gpt_output}")