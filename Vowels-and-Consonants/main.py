#
# Jay
# 4/19/2025
# Vowels and Consonants Programming Project
# COSC 1010
#

# Define a set containing all vowels 
vowels = set("aeiouAEIOU")

# Function to count the number of vowels in a given string
def count_vowels(input_string):
    vowel_count = 0  
    for char in input_string:  
        if char in vowels:  
            vowel_count += 1  
    return vowel_count   

# Function to count the number of consonants in a given string
def count_consonants(input_string):
    consonant_count = 0  
    for char in input_string:  
        if char.isalpha() and char not in vowels:  
            consonant_count += 1  
    return consonant_count  

# Prompt the user to enter a string
user_input = input("Enter a string to count vowels and consonants: ")
vowel_count = count_vowels(user_input)
consonant_count = count_consonants(user_input)
print("Number of vowels in the string are: ", vowel_count)
print("Number of consonants in the string are: ", consonant_count)



