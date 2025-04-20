import streamlit as st

st.title("Simple Calculator")
st.write("This is a Simple Calculator that Can Perform Addition, Substraction, Multiplication, Division")

def Calculator( num1,num2,operator) :

   if operator == "add":
      return num1 + num2
   
   elif operator == "subtract":
      return num1 - num2
   
   elif operator == "multiply":
      return num1 * num2
   
   elif operator == "divide":
      return num1 / num2
   

num1 = st.number_input("Enter First Number :", value=0)
num2 = st.number_input("Enter Second Number :", value=0)
operator = st.radio("Select Operator :",('add', 'subtract', 'multiply', 'divide'))

if st.button("Calculate") :
   try:
      result = Calculator(num1, num2, operator)
      st.write(f"The Result of {num1} {operator} {num2} is : {result}")

   except ZeroDivisionError as e:
     st.error(e)

   except ValueError as e:
     st.error(e)

   except Exception as e:
     st.error(f"Error Occured : {e} ")

