import streamlit as st

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Set page title and configure layout
st.set_page_config(page_title="Simple Calculator", layout="centered")

# Display calculator title
st.title("Simple Calculator")

# Get user input
num1 = st.number_input("Enter the first number:")
operation = st.selectbox("Select an operation:", ("Addition", "Subtraction", "Multiplication", "Division"))
num2 = st.number_input("Enter the second number:")

# Perform calculation based on user-selected operation
result = 0
if operation == "Addition":
    result = add(num1, num2)
elif operation == "Subtraction":
    result = subtract(num1, num2)
elif operation == "Multiplication":
    result = multiply(num1, num2)
elif operation == "Division":
    result = divide(num1, num2)

# Display the result
st.write("Result:", result)

"""
The code begins by importing the necessary libraries, streamlit.
The mathematical operations (addition, subtraction, multiplication, and division) are defined as separate functions to perform the respective calculations.
The Streamlit page is configured with a title and layout settings.
The calculator's title is displayed using st.title().
User input is obtained using st.number_input() to enter the first and second numbers.
The operation selection is provided using st.selectbox(), where the user can choose from the available options.
After obtaining the user's input, the code determines which operation was selected and calls the corresponding function to perform the calculation.
The result is stored in the result variable.
Finally, the result is displayed on the page using st.write().

"""