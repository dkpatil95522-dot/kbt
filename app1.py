import streamlit as st

st.title("Simple input app")

name =st.text_input("Enter Your Name:")

if st.button("submit"):
    st.write("hello " , name)