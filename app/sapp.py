import streamlit as st
import requests


url = "http://127.0.0.1:8000/ask"

st.header('ZV1 assistant : What can I do for you ?')

in_question = st.text_input("Enter your question here")




if st.button("Search"):
    st.success("I am searching!")
    # if a question is entered, and the button search is clicked, we then request the assistant

    if in_question.strip():
        response = requests.get(url,params={"question":in_question})
        answer = response.json().get('zv1_assistant')
        st.text("zv1 bot : " + answer)
