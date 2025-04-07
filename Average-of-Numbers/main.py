#
# Jay 
# 4/5/25
# Average of Numbers Programming Project
# COSC 1010
#

def main():
    numbersFile = open ("numbers.txt", "r")

    total = 0 
    numbersOfLines = 0
    line = numbersFile.readline()

    average = total / numbersOfLines

    print("The average is", average)

main()