#
# Jay 
# 4/5/25
# Average of Numbers Programming Project
# COSC 1010
#

def main():
    try:
        with open("numbers.txt", "r") as numbersFile:
            total = 0
            numberOfLines = 0
            for line in numbersFile:
                try:
                    number = float(line.strip())
                    total += number
                    numberOfLines += 1
                except ValueError:
                    print(f"Invalid number in file: {line.strip()}")
            if numberOfLines > 0:
                average = total / numberOfLines
                print("The average is", average)
            else:
                print("No valid numbers to calculate an average.")
    except FileNotFoundError:
        print("Error: The file 'numbers.txt' was not found.")
main()