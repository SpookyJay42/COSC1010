#
# Jay
# 02/23/2025
# Areas of Rectangles Programming Project
# COSC 1010
#
# Local variables
lenght2 = 0
lenght1 = 0
width1 = 0
width2 = 0
area1 = 0 
area2 = 0

# Get length A
lenght1 = int(input ('Enter the lenght of rectangle 1: '))

# Get width A
width1 = int(input('Enter the width of rectangle 1: ')) 

# Get length B
lenght2 = int(input('Enter the lengh of rectangle 1: '))

# Get width B
width2 = int(input('Enter the width of rectangle 1: ')) 

# Calculate area A
area1 = lenght1 * width1

# Calculate area B
area2 = lenght2 * width2

# Print area comparison using if-elif-else statements
if area1 > area2:
    print('Rectangle 1 has the greater area.')
elif area2 > area1:
    print('Rectangle 2 has the greater area.')
else: 
    print('Both have the same area.')