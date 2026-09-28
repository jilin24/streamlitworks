import streamlit as st
from datetime import date

st.title("Student Registration Form")

name=st.text_input("Name")
age=st.number_input("Age",min_value=0)
dob=st.date_input("Date of Birth", min_value=date(1990,1,1),max_value=date.today(),value=date(2000,1,1))
email=st.text_input("Email")
gender=st.radio("Gender",['Male','Female'])
courses=st.selectbox("Courses",['Python','Java','DotNet','Testing'])
btn = st.button("Register")

if btn:
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Date of Birth:", dob)
    st.write("Email:",email)
    st.write("Gender:", gender)
    st.write("Courses:",courses)