#
# Jay
# 4/5/25
# Exception Handling Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

def main():
    try:
        with open("number.txt", "r") as numbersFile:
            total = 0
            numbersOfLines = 0 
            for line in numbersFile:
                try:
                    number = int(line.strip())
                    total += number
                    numbersOfLines += 1
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
            if numbersOfLines == 0:
                raise ValueError("The file is empty or contrains no valid numbers.")
            average = total / numbersOfLines
    except IOError:
        print("An IOError has occurred.")
    except ValueError as error:
        print(f"A ValueError aoccurred: {error}")
    else:
        print(f"The average is {average}")
    finally:
        print("End of program")
main()
