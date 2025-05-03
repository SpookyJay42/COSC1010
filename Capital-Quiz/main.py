#
# Jay
# 4/26/2025
# Capital Quiz Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

import random


    # Initialize dictionary
capitals = {'Alabama':'Montgomery', 'Alaska':'Juneau',
                'Arizona':'Phoenix', 'Arkansas':'Little Rock',
                'California':'Sacramento', 'Colorado':'Denver',
                'Connecticut':'Hartford', 'Delaware':'Dover',
                'Florida':'Tallahassee', 'Georgia':'Atlanta',
                'Hawaii':'Honolulu', 'Idaho':'Boise',
                'Illinois':'Springfield', 'Indiana':'Indianapolis',
                'Iowa':'Des Moines', 'Kansas':'Topeka',
                'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge',
                'Maine':'Augusta', 'Maryland':'Annapolis',
                'Massachusetts':'Boston', 'Michigan':'Lansing',
                'Minnesota':'Saint Paul', 'Mississippi':'Jackson',
                'Missouri':'Jefferson City', 'Montana':'Helena',
                'Nebraska':'Lincoln', 'Nevada':'Carson City',
                'New Hampshire':'Concord', 'New Jersey':'Trenton',
                'New Mexico':'Santa Fe', 'New York':'Albany',
                'North Carolina':'Raleigh', 'North Dakota':'Bismarck',
                'Ohio':'Columbus', 'Oklahoma':'Oklahoma City',
                'Oregon':'Salem', 'Pennsylvania':'Harrisburg',
                'Rhode Island':'Providence', 'South Carolina':'Columbia',
                'South Dakota':'Pierre', 'Tennessee':'Nashville',
                'Texas':'Austin', 'Utah':'Salt Lake City',
                'Vermont':'Montpelier', 'Virginia':'Richmond',
                'Washington':'Olympia', 'West Virginia':'Charleston',
                'Wisconsin':'Madison', 'Wyoming':'Cheyenne'
}
def main():
    score = 0
    question_count = 15
    print("Welcome to the State Capitals Quiz!")
    print("Type 'quit' to exit the game at any time.\n")

    # Continue until user quits the game.
    while True:
        state = random.choice(list(capitals.keys()))
        capital = capitals[state]  # Corrected variable usage
        
        user_answer = input(f"What is the capital of {state}? ").strip()

        if user_answer.lower() == 'quit':
            print("Thanks for playing! Bye Bye!!")
            print(f"You scored {score} out of 10.")
            break
        if user_answer == capital:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The capital of {state} is {capital}.\n")

# Call the main function.
if __name__ == "__main__":
    main()