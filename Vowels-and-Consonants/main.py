#
# Jay
# 4/19/2025
# Vowels and Consonants Programming Project
# COSC 1010
#

vowels ="aeiouAEIUO"
def count_vowels(input_string):
    vowel_count = 0
    for char in input_string:
        if char in vowels:
            count_vowel +=1
    return vowel_count
def count_consonants(input_string):  
    consonant_count = 0
    for char in input_string:
        if char.isalpha() and char not in vowels:
            consonant_count += 1
    return consonant_count

user_input = input("Enter a string: ")
vowel_count = count_vowels(user_input)
consonant_count = count_consonants(user_input)

print("Number of vowels in string are: ", vowel_count)
print("Number of consonants in the sting are ",consonant_count)



