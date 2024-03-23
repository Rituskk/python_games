import random
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome_message():
    print("""
           ______________________________________
          |                                      |
          | Welcome to the Number Guessing Game! |
          |______________________________________|
          """)

def get_range():
    while True:
        try:
            lower = int(input("Enter the lower bound of the range: "))
            upper = int(input("Enter the upper bound of the range: "))
            if lower >= upper:
                print("The lower bound must be less than the upper bound.")
            elif lower < 0 or upper < 0:
                print("The lower and upper bounds must be positive.")
            elif upper - lower < 10:
                print("The range must be at least 10.")
            else:
                return int(lower), int(upper)
        except ValueError:
            print("Please enter a valid number.")

def number_guessing():
    lower, upper = get_range()
    number = random.randint(lower, upper)
    attempts = 0
    if upper - lower == 10:
        maxAttempts = 5
    else:
        maxAttempts = 10
    print(f"\nI'm thinking of a number between {lower} and {upper}. Can you guess it?")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
            if attempts == maxAttempts:
                print(f"Sorry, you have reached the maximum number of attempts. The number was {number}.")
                break
        except ValueError:
            print("Please enter a valid number.")
        
def main():
    clear_terminal()
    welcome_message()
    while True:
        number_guessing()
        play_again = input("\nWould you like to play again? (y/n): ")
        if play_again.lower() != 'y':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
    
