#
# Jay
# 03/09/2025
# Feet to Inches Programming Project
# COSC 1010
#
#Variables 
feet_to_inches = 0
inches = 0
feet = 0
# Main Function
def feet_to_inches(feet):
    #Get a number of feet from the user.
    inches = (feet / 1 ) * 12
    return inches 
# The feet_to_inches function converts feet to inches.
def main():
    feet = float(input(" Please enter the number of feet: "))
    inches = feet_to_inches(feet)
    print( "\n" + str (feet), "Feel converted to inches is", format(inches, ".2f"), "inches")

main()