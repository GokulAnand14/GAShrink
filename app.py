import streamlit as st
import requests

st.title("GAShrink")
inp_text = st.text_input("Enter your text")
button = st.button("⚡️ Do Magic ⚡️")

if button:
    with st.spinner():
        response_json = requests.post("https://gokul14-gashrink.hf.space/run/predict", json={
        "data": [
            inp_text,
        ]}).json()
        md = f"""{response_json['data'][0]}"""
        st.markdown(
            md,
            unsafe_allow_html=True,
        )