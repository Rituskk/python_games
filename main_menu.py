import os
import importlib.util

def load_game(game_name):
    game_path = os.path.join('quiz_game', f'{game_name}.py')
    spec = importlib.util.spec_from_file_location(game_name, game_path)
    game_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(game_module)
    return game_module.Game()

def main():
    while True:
        print("Main Menu")
        print("1. Quiz Game")
        print("0. Exit")
        
        choice = input("Choose a game (0-1): ")
        
        if choice == '1':
            game = load_game('quiz_game')
            game.play()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 0 or 1.")

if __name__ == "__main__":
    main()
