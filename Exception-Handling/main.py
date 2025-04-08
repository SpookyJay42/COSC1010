#
# Jay
# 4/5/25
# Exception Handling Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
def main():
    try:
        numbersFile = open("number.txt", "r")
        total = 0
        numbersOfLines = 0
        line = numbersFile.readline()
        while line != "":
         numberOfLines += 1
         total += int(line)
         line = numbersFile.readline()
    
        average = total / numberOfLines
    except IOError as error:
        print( "An IOError has occured")
    except ValueError as error:
        print( "A ValueError occured" )
    else:
         print("The average is")
    finally: 
        print("End of program")

main()