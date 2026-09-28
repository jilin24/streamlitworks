import streamlit as st

st.title("User Information")

name = st.text_input("Enter your name")

age = st.number_input("Enter your age", min_value=1, max_value=100)

gender = st.selectbox(
    "Select gender",
    ["Male", "Female", "Other"]
)

qualification = st.selectbox(
    "Select qualification",
    ["Degree", "Diploma", "Other"]
)

btn = st.button("Submit")

if btn:
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Gender:", gender)
    st.write("Qualification:", qualification)