#
# Name
# Date
# Lottery Number Generator Programming Project
# COSC 1010
#
# 
import random

MAX_DIGITS = 7
START = 0
END = 9

def main():
    numbers = [0] * 7

    for index in range (MAX_DIGITS):
        numbers[index] = random.randint(START, END)

    print("Here are your lottery numbers:")
    for index in range (MAX_DIGITS):
        print(numbers[index], end='')
    print()
main()