#
# Jay
# 4/5/25
# File Display Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
def main():
    numbersFile = open("numbers.txt", "r")

    line = numbersFile.readline()

    while line != "":
        print(line.rstrip("\n"))
        line = numbersFile.readline()

main()