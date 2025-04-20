import streamlit as st

st.title("BMI Calculator")
st.write("Enter Your Height and Weight to Calculate Your BMI")

height = st.number_input(
    "Height (in Meters)", min_value=0.5, max_value=3.0, value=1.75)

weight = st.number_input(
    "Weight (in Kilograms)", min_value=10, max_value=100, value=70)

if st.button("Calculate BMI") :
    if height > 0 and weight > 0 :
       bmi = weight / (height ** 2)
       st.success(f"Your BMI is : {bmi:2f}")

       if bmi > 18.5 :
           st.warning("You are Under Weight")

       elif bmi > 24.9 :
           st.warning("Normal Weight")

       elif bmi > 30.2 :
           st.warning("Over Weight")

       else :
           st.error("You are Obese")

    else :
      st.error("Enter Valid Height and Weight Values.")
