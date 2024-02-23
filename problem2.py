"""
Matthew Daguanno
2024-02-23
This program finds the difference in age then apples it to the last age given to find the third childs age
"""

# Asks for the first two childrens ages
youngest = int(input("What is the youngest childs age?: "))
middle = int(input("What is the middle childs age?:"))

# Subtract the middle childs age from the yougest childs age to find the difference
dif = int(middle) - int(youngest)

# Add the difference to the middle childs age
oldest = int(middle) + int(dif)

# Prints the oldest childs age
print("The oldest child will be " + str(oldest) + " years old")