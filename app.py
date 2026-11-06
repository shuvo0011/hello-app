import streamlit as st
from logic import greet

st.title("Hello App")

name = st.text_input("Your name")
if name:
    st.write(greet(name))

a = st.number_input("First number")
b = st.number_input("second number")

st.write(f.Sum: {add(a,b)})