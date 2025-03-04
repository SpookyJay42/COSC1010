#
# Jay
# 03/03/2025
# Budget Analysis Programming Project
# COSC 1010

# Variables 
userBudget = 0
moreExpenses = 0
userTotalExpenses = 0
userExpenses = 0
totalExpenses = 0

userBudget = float( input( "Please enter how much you've budgeted " + \
                           "for the month: " ))
moreExpenses = "y"
userTotalExpenses = 0

while moreExpenses == "y":
    userExpenses = float(input("Enter an expense: "))
    userTotalExpenses += userExpenses
    moreExpenses = input("Do you have more expenses?: Type y "+ \
                         "For yes, any key for no: " )
if userTotalExpenses > userBudget: 
    print("You were over your budget of","$", format(userBudget, ",.2f"), \
          "by $",format(userTotalExpenses - userBudget, ",.2f"))
elif userBudget > totalExpenses: 
    print("You were under your budget of","$" + format (userBudget, ",.2f"), \
            "by $", format(userBudget - userTotalExpenses, ",.2f"))
else: 
    print("You uses exactly your budget of","$", \
          format(userBudget, ",.2f"), ".")