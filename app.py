import random

# Specification: The winner of the game is determined by these three rules:
# 1. Rock beats Scissors.
# 2. Scissors beats Paper.
# 3. Paper beats Rock.
# The game will be played in a best of 3 format.
# The game will be played between the user and the computer.
# The computer will randomly select rock, paper, or scissors.
# The user will be prompted to select rock, paper, or scissors.
# The winner of the game will be displayed after each round.
# The overall winner of the game will be displayed after 3 rounds.
# The user will be prompted to play again or quit.
# The user can play as many times as they want.
# The user can quit at any time.
# The user can see the rules of the game at any time.
# The user can see the current score at any time.
# The user can see the current round at any time.
# The user can see the current game status at any time.
# The user can see the current game winner at any time.
# The user can see the current game history at any time.
# The user can see the current game rules at any time.
# The user can see the current game instructions at any time.
# The user can see the current game information at any time.
# The user can see the current game settings at any time.
# The user can see the current game statistics at any time.
# The user can see the current game details at any time.
# The user can see the current game results at any time.
# The user can see the current game summary at any time.
def play_game():
    # Initialize game variables
    score = {'user': 0, 'computer': 0}
    round_num = 1
    game_history = []
    
    # Game loop
    while True:
        print(f"Round {round_num}")
        
        # Prompt user for their choice
        user_choice = input("Enter your choice (rock, paper, scissors): ")
        
        # Generate computer's choice
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        
        # Determine the winner of the round
        round_winner = determine_winner(user_choice, computer_choice)
        
        # Update score and game history
        if round_winner == 'user':
            score['user'] += 1
        elif round_winner == 'computer':
            score['computer'] += 1
        game_history.append((user_choice, computer_choice, round_winner))
        
        # Display round results
        print(f"User choice: {user_choice}")
        print(f"Computer choice: {computer_choice}")
        print(f"Round winner: {round_winner}")
        
        # Check if game is over
        if score['user'] == 2 or score['computer'] == 2:
            break
        
        # Increment round number
        round_num += 1
    
    # Determine the overall winner of the game
    game_winner = determine_game_winner(score)
    
    # Display game results
    print("Game over!")
    print(f"User score: {score['user']}")
    print(f"Computer score: {score['computer']}")
    print(f"Game winner: {game_winner}")
    print("Game history:")
    for round_result in game_history:
        print(f"User choice: {round_result[0]}, Computer choice: {round_result[1]}, Round winner: {round_result[2]}")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'scissors' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def determine_game_winner(score):
    if score['user'] > score['computer']:
        return 'user'
    elif score['user'] < score['computer']:
        return 'computer'
    else:
        return 'tie'

play_game()