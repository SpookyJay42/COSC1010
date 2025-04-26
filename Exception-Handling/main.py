#
# Jay
# 4/5/25
# Exception Handling Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
 
import os
def main():
    try:
        # Check if the file exists before attempting to open it
        if not os.path.exists("number.txt"):
            raise FileNotFoundError("The file 'number.txt' does not exist in the current directory.")
        
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
                raise ValueError("The file is empty or contains no valid numbers.")
            
            average = total / numbersOfLines
    except FileNotFoundError as fnf_error:
        print(f"FileNotFoundError: {fnf_error}")
    except IOError:
        print("An IOError has occurred while trying to read the file.")
    except ValueError as error:
        print(f"A ValueError occurred: {error}")
    else:
        print(f"The average is {average}")
    finally:
        print("End of program")

main()
