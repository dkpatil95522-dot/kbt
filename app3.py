import streamlit as st

st.title("Basic Calculator")

num1 = st.number_input("Enter first number", value=0, step=1)
num2 = st.number_input("Enter second number", value=0, step=1)

operation = st.selectbox("Choose operation", ["add", "sub", "mul", "div"])

if st.button("Calculate"):

    if operation == "add":
        st.write("Result:", num1 + num2)

    elif operation == "sub":
        st.write("Result:", num1 - num2)

    elif operation == "mul":
        st.write("Result:", num1 * num2)

    elif operation == "div":
        if num2 != 0:
            st.write("Result:", num1 // num2)   # integer division
        else:
            st.write("Cannot divide by zero")