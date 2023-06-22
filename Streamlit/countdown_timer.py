import streamlit as st
import time

# Set page title and configure layout
st.set_page_config(page_title="Countdown Timer", layout="centered")

# Display application title and description
st.title("Countdown Timer")
st.write("Enter the duration in seconds and click 'Start' to begin the countdown.")

# Get user input for the duration
duration = st.number_input("Enter the duration in seconds:", min_value=1, step=1)

# Initialize the countdown variable
countdown = None

# Function to update the countdown display
def update_countdown():
    global countdown

    if countdown is not None:
        st.write("Time remaining:", countdown, "seconds")

        if countdown > 0:
            countdown -= 1
            time.sleep(1)  # Wait for 1 second
            update_countdown()
        else:
            st.write("Countdown completed!")

# Start the countdown
if st.button("Start"):
    countdown = duration
    update_countdown()
