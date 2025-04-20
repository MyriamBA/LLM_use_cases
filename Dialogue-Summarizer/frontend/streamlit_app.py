import streamlit as st
import requests

API_URL = "http://backend:8000/summarize"  # for Docker Compose (or localhost:8000 for local)

st.title("Dialogue Summarizer")
st.write("Enter a dialogue below to get a summary:")

dialogue_input = st.text_area("Enter Dialogue:", height=200, placeholder="Paste your dialogue here...")

if st.button("Summarize"):
    if dialogue_input.strip() == "":
        st.warning("Please enter a dialogue to summarize!")
    else:
        with st.spinner("Generating Summary..."):
            response = requests.post(API_URL, json={"dialogue": dialogue_input})
            if response.status_code == 200:
                st.success("Summary Generated!")
                st.write(response.json()["summary"])
            else:
                st.error("Error generating summary.")
