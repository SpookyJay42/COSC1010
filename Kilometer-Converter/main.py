#
# Jay
# 03/05/2025
# Kilometer Converter Programming Project
# COSC 1010

# Main function.
def kilometers_to_miles(kilometers):
  miles = kilometers * 0.621371
  return miles
# The kilometers_to_miles function converts kilometer to miles.
def main():
    kilometers = float(input("Enter the distance in kilometers: "))
    miles = kilometers_to_miles(kilometers)
    print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")

main()