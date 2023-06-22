import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.player_score = 0
        self.computer_score = 0

    def play(self, player_choice):
        # Randomly select the computer's choice
        computer_choice = random.choice(self.choices)

        # Validate the player's choice
        if player_choice not in self.choices:
            raise ValueError("Invalid choice. Please select 'rock', 'paper', or 'scissors'.")

        # Determine the result based on the choices
        if player_choice == computer_choice:
            result = "It's a tie!"
        elif (
            (player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "paper" and computer_choice == "rock") or
            (player_choice == "scissors" and computer_choice == "paper")
        ):
            # Player wins
            self.player_score += 1
            result = "You win!"
        else:
            # Computer wins
            self.computer_score += 1
            result = "Computer wins!"

        return result, computer_choice
