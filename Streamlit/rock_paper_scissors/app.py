import streamlit as st
from game import RockPaperScissors

# Set page title and configure layout
st.set_page_config(page_title="Rock Paper Scissors", layout="centered")

# Display application title and description
st.title("Rock Paper Scissors Game")
st.write("Choose your move and see if you can beat the computer!")

# Create an instance of the game
game = RockPaperScissors()

# Get user input
player_choice = st.selectbox("Select your move:", game.choices)

# Play the game
if st.button("Play"):
    try:
        # Call the play method to determine the result and computer's choice
        result, computer_choice = game.play(player_choice)
        
        # Display the player's and computer's choices
        st.write("You chose:", player_choice)
        st.write("Computer chose:", computer_choice)
        
        # Display the result and scores
        st.write(result)
        st.write("Player Score:", game.player_score)
        st.write("Computer Score:", game.computer_score)
    except ValueError as e:
        # Handle invalid choices by displaying an error message
        st.write("Error:", str(e))
