import json
import curses


def display_score(stdscr, score):
    stdscr.clear()  # Clear the screen
    stdscr.addstr(0, 0, f"Score: {score}", curses.A_REVERSE)  # Add score at top of screen
    stdscr.refresh()  # Refresh the screen
    
# Function to display a welcome message
def display_welcome_message(stdscr):
    stdscr.clear()  # Clear the screen
    stdscr.addstr(0, 0, """
                  _________________________
                  
                  Welcome to the Quiz Game!
                  _________________________
                  """, curses.A_BOLD)  # Add welcome message
    stdscr.addstr(12, 0, "Press any key to start...")  # Add instruction to start
    stdscr.refresh()  # Refresh the screen
    curses.noecho()  # Don't display user input
    stdscr.getch()  # Wait for user input to start
    stdscr.addstr('\n\nOkay! Let\'s play :)')
    stdscr.refresh()  # Refresh the screen
    curses.echo()  # Display user input again (after the game starts)
    
def taking_input(stdscr):

    return selected_answer
    
with open('questions.json') as f:
    data = json.load(f)

# Initialize curses
stdscr = curses.initscr()
curses.cbreak()  # React to keys instantly, without waiting for Enter to be pressed
stdscr.keypad(True)  # Enable keypad mode
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Define color pair 1 (green text on black background)
curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # Define color pair 2 (red text on black background)

score = 0
playing = True
    
try:
    while playing:
        display_welcome_message(stdscr)
        curses.napms(1000)
        
        for question in data['questions']:
            display_score(stdscr, score) 
            stdscr.addstr(f"\nQuestion number: {question['id']}\n")
            stdscr.addstr(f"Question: {question['question']}\n")

            stdscr.addstr("Possible answers: \n\n")

            for index, answer in enumerate(question['answers']):
                stdscr.addstr(f"{index + 1}) {answer['text']} \n")
            
            while True:
                stdscr.addstr("\nPlease select the correct answer (by typing the number): ")
                selected_answer = stdscr.getstr().decode()
                if not selected_answer.isdigit() or int(selected_answer) < 1 or int(selected_answer) > len(question['answers']):
                    stdscr.addstr("\nInvalid answer! Please try again.")
                    curses.napms(200)
                else:
                    break
            
            selected_answer = int(selected_answer) - 1        
            if question['answers'][selected_answer]['correct']:
                stdscr.attron(curses.color_pair(1)) 
                stdscr.addstr('\nCongratulations! You are correct!')
                stdscr.attroff(curses.color_pair(1))
                score += 1
                stdscr.refresh()
                
            else:
                stdscr.attron(curses.color_pair(2)) 
                stdscr.addstr('\nSorry, you are wrong!')
                stdscr.attroff(curses.color_pair(2)) 
                stdscr.refresh()
                
            curses.napms(1500)
            stdscr.refresh()


        stdscr.addstr('\n\nCalculating results...')
        curses.napms(1000)
        stdscr.refresh()
        stdscr.addstr(f"\nYour final score is: {score}")
        if score < 10:
            stdscr.addstr("\nBetter luck next time!")
        else:
            stdscr.addstr("\nGreat job!")
        
        curses.napms(300)
        stdscr.addstr("\n\nWould you like to play again? (y/n): ")
        if stdscr.getstr().decode().lower() != 'y':
            playing = False
        else:
            score = 0
            stdscr.clear()
            stdscr.refresh()
            curses.napms(500)
        
finally:
    stdscr.clear()
    curses.nocbreak()
    stdscr.keypad(False)
    curses.endwin()

print("Thanks for playing!")