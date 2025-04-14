#
# Name
# Date
# Magic 8 Ball Programming Project
# COSC 1010
#
# 
import random

answers = [
    "Yes",
    "No",
    "Maybe",
    "Ask again later",
    "Definitely",
    "Absolutely not",]

print("Your lucky number is", random.randint(1, 100))

while True:
    x = input("\nAsk a yes or no question and press enter > ")
    print(random.choice(answers))
