import random

# define the choices array
choices = ["Rock", "Paper", "Scissors"]

def main():
    try:
        user_input = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()

        # validate user input
        if user_input not in choices:
            raise ValueError("Invalid choice. Please enter Rock, Paper, or Scissors.")

        # convert the user input to an index
        player_choice = choices.index(user_input)

        # randomly select the computer choice
        computer_choice = random.randint(0, 2)

        print(f"Player's choice: {choices[player_choice]}")
        print(f"Computer's choice: {choices[computer_choice]}")

        # determine the winner
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 0 and computer_choice == 2) or \
                (player_choice == 1 and computer_choice == 0) or \
                (player_choice == 2 and computer_choice == 1):
            print("You win!")
        else:
            print("You lose!")

    except ValueError as e:
        print(f"Error: {e}")

# run the game
if __name__ == "__main__":
    main()
