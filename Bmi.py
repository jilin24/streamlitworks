import streamlit as st

st.title("BMI Calculator")

weight = st.number_input("Enter weight in kg", min_value=0.0)

height = st.number_input("Enter height in cm", min_value=0.0)

btn = st.button("Calculate BMI")

if btn:
    height_m = height / 100
    bmi = weight / (height_m * height_m)

    st.write("BMI is", round(bmi, 2))

    if bmi < 18.5:
        st.write("Underweight")
    elif bmi < 25:
        st.write("Normal weight")
    elif bmi < 30:
        st.write("Overweight")
    else:
        st.write("Obese")