import random
import time
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome_message():
    print("""
           ______________________________________
          |                                      |
          | Welcome to the Rock, Paper, Scissors |
          |             Game!                    |
          |______________________________________|
          """)
    
options = ['r', 'p', 's']
colors = {
    'green': '\033[92m',
    'red': '\033[91m',
    'white': '\033[0m'
}

class User:
    def __init__(self):
        self.score = 0
        self.choice = None
        
    def choose(self):
        while True:
            choice = input("Choose rock(r), paper(p), or scissors(s): ").lower()
            if choice in options:
                self.choice = choice
                break
            else:
                print("Invalid choice. Please choose rock, paper, or scissors.")
      
class Computer:
    def __init__(self):
        self.score = 0
        self.choice = None
        
    def choose(self):
        self.choice = random.choice(options)

def check_game_over(value_to_check, current_round, message):
    if current_round + value_to_check == 5:
        print(message)
        return True
    return False
                
def check_winner(user, computer, current_round):
    current_round += 1
    if user.choice == computer.choice:
        print("\n\nIt's a tie!")
    elif user.choice == 'r' and computer.choice == 's':
        print(f"\n\n{colors['green']}You win this round!{colors['white']}")
        user.score += 1
        if check_game_over(user.score, current_round, "Congratulations! You win the game!"):
            return
    elif user.choice == 'p' and computer.choice == 'r':
        print(f"\n\n{colors['green']}You win this round!{colors['white']}")
        user.score += 1
        if check_game_over(user.score, current_round, "Congratulations! You win the game!"):
            return
    elif user.choice == 's' and computer.choice == 'p':
        print(f"\n\n{colors['green']}You win this round!{colors['white']}")
        user.score += 1
        if check_game_over(user.score, current_round, "Congratulations! You win the game!"):
            return
    else:
        print(f"\n\n{colors['red']}Computer wins this round!{colors['white']}")
        computer.score += 1
        if check_game_over(computer.score, current_round, "Computer wins the game!"):
            return
    
    print("\n\n\nSummary:")
    print(f"\nYour score: {user.score}")
    print(f"Computer's score: {computer.score}")
    print(f"Round {current_round} complete.")
    
def game_loop():
    current_round = 1
    user = User()
    computer = Computer()
    
    while True:
        user.choose()
        computer.choose()
    
        print(f"\nYou chose: {user.choice}")
        print(f"Computer chose: {computer.choice}")
        check_winner(user, computer, current_round)
        print(f"\nEnd of round {current_round}.")
        current_round += 1
        time.sleep(2.5)
        clear_terminal()
        welcome_message()
        print(f'\nRound: {current_round}.')
        print(f"\nUser score: {colors['green'] if user.score > computer.score else colors['red']} {user.score} {colors['white']}")
        print(f"Computer score: {colors['green'] if user.score > computer.score else colors['red']} {computer.score} {colors['white']}\n")
        
        if current_round == 5:
            if user.score > computer.score:
                print("\nCongratulations! You win the game!")
            elif user.score < computer.score:
                print("\nComputer wins the game!")
            else:
                print("\nIt's a tie game!")

            play_again = input("\nDo you want to play again? (y/n): ").lower()
            if play_again != 'y':
                break
            else: 
                user.score = 0
                computer.score = 0
                current_round = 1
                clear_terminal()
                welcome_message()
                print("\nLet's play 5 rounds to decide who wins!\n")
        
def main():
    clear_terminal()
    welcome_message()
    print("\nLet's play 5 rounds to decide who wins!\n")
    game_loop()
    print("Thanks for playing!")
    
if __name__ == "__main__":
    main()