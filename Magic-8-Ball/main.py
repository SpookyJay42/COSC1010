#
# Name
# Date
# Magic 8 Ball Programming Project
# COSC 1010
#
# 

import random  # Importing the random module to generate random numbers and choices

# Load the list of possible answers from a text file
with open("answers.txt", "r") as file:
    answers = [line.strip() for line in file if line.strip()]  

# Generate and display a random lucky number between 1 and 100
print("Your lucky number is", random.randint(1, 100))

# Infinite loop to continuously prompt the user for questions
while True:
    # Prompt the user to ask a yes/no question
    x = input("\nAsk a yes or no question and press enter > ")
    
    # Provide a random answer from the list of answers
    print(random.choice(answers))
