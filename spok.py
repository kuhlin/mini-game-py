import random

# Specification: The winner of the game is determined by these rules:
# 1. Scissors beats Paper.
# 2. Paper beats Rock.
# 3. Rock beats Lizard
# 4. Lizard beats Spock
# 5. Spock beats Scissors
# 6. Scissors beats Lizard
# 7. Lizard beats Paper
# 8. Paper beats Spock
# 9. Spock beats Rock
# 10. Rock beats Scissors
# The game will be played in a best of 5 format.
# The game will be played between the user and the computer.
# The computer will randomly select rock, paper, scissors, lizard, or spock.
# The user will be prompted to select rock, paper, scissors, lizard, or spock.
# The winner of the game will be displayed after each round.
# The overall winner of the game will be displayed after 5 rounds.
# The user will be prompted to play again or quit.
# The user can play as many times as they want.
# The user can quit at any time.
# The user can see the rules of the game at any time.
# The user can see the current score at any time.
# The user can see the current round at any time.
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "rock" and computer_choice == "lizard") or (user_choice == "lizard" and computer_choice == "spock") or (user_choice == "spock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "lizard") or (user_choice == "lizard" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "spock") or (user_choice == "spock" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    while round_number <= 5:
        print(f"Round {round_number}")
        print("Enter your choice: rock, paper, scissors, lizard, or spock")
        user_choice = input().lower()

        while user_choice not in ["rock", "paper", "scissors", "lizard", "spock"]:
            print("Invalid choice. Please enter rock, paper, scissors, lizard, or spock")
            user_choice = input().lower()

        computer_choice = random.choice(["rock", "paper", "scissors", "lizard", "spock"])
        print(f"Computer chooses: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        print(winner)

        if winner == "You win!":
            user_score += 1
        elif winner == "Computer wins!":
            computer_score += 1

        print(f"Score: You {user_score} - {computer_score} Computer")

        round_number += 1

    if user_score > computer_score:
        print("You are the overall winner!")
    elif user_score < computer_score:
        print("Computer is the overall winner!")
    else:
        print("It's a tie!")

def main():
    print("Welcome to Rock-Paper-Scissors-Lizard-Spock Game!")
    print("Type 'rules' to see the rules of the game.")
    print("Type 'score' to see the current score.")
    print("Type 'round' to see the current round.")
    print("Type 'quit' to exit the game.")

    while True:
        print("Enter your choice:")
        choice = input().lower()

        if choice == "rules":
            print("The winner of the game is determined by these rules:")
            print("1. Scissors beats Paper.")
            print("2. Paper beats Rock.")
            print("3. Rock beats Lizard.")
            print("4. Lizard beats Spock.")
            print("5. Spock beats Scissors.")
            print("6. Scissors beats Lizard.")
            print("7. Lizard beats Paper.")
            print("8. Paper beats Spock.")
            print("9. Spock beats Rock.")
            print("10. Rock beats Scissors.")
        elif choice == "score":
            print(f"Score: You {user_score} - {computer_score} Computer")
        elif choice == "round":
            print(f"Round {round_number}")
        elif choice == "quit":
            print("Thanks for playing!")
            break
        else:
            play_game()

if __name__ == "__main__":
    main()