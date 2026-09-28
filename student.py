import streamlit as st

st.title("User Information")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=1, max_value=100)
dob= st.date_input("Enter your date of birth", min_value=0, max_value=100)
email = st.text_input("Enter your email")
gender = st.selectbox(
    "Select gender",
    ["Male", "Female", "Other"]
)
courses=st.selectbox("select course",['python','java','dotnet','testing'])


btn = st.button("Register")

if btn:
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("dob:", dob)
    st.write("Email:", email)
    st.write("Gender:", gender)
    st.write("courses:", courses)