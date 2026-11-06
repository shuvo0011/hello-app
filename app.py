import streamlit as st

from logic import greet

st.title("Hello App")

st.write(greet())

name = st.text_input("Your name")

if name:
    st.write(greet(name))