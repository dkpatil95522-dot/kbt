import streamlit as st

st.title("Welcome to Basic Streamlit App")

age = st.slider("Select your age", 1, 100)
city = st.selectbox("Select your city", ["Delhi", "Mumbai", "Nashik", "Pune","Dhule"])

if st.button("Show Details"):
    st.write("Your Age is:", age)
    st.write("Your City is:", city)