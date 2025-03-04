#
# Jay 
# 03/03/2025
# Bug Collector Programming Project
# COSC 1010

# Initialize variables for bugs and total number of bugs collected.
total = 0 
# Get number of bugs collected each day using a for loop.
for day in range (1, 8):
    # Prompt the user.
    print('Enter the bugs collected on day', day)
   
    # Input the number of bugs.
    bugs = int(input())
    total += bugs

# Display the total number of bugs collected.
print('you collected a total of', total, 'bugs.')