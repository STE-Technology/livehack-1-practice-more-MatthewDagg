"""
Matthew Daguanno
2024-02-23
This program asks for the boiling point, then does calculations to find the atmospheric pressure
"""
# Asks for the boiling point
boiling_point = int(input("What is the boiling point?: "))

# Puts input into calculation
pressure = 5 * (boiling_point) - 400

# Prints the atmospheric pressure
print("The atmospheric pressure is: " + str(pressure))