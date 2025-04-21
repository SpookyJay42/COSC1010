#
# Name
# Date
# Pig Latin Programming Project
# COSC 1010
#
# 
def piglatin():
    words = input("Input sentence: ").split()
    for word in words:
        print(word[1:] + word[0] + "ay", end=' ')

piglatin()