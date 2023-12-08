# Python

# Script Name:                  Ops Challenge: Python Conditional Statements
# Author:                       Kevin Hoang
# Date of latest revision:      12/07/2023
# Purpose:                      Python script with if statements with conditional statements
# Execution:                    OpsChallenge09.py
# Resources:                    https://chat.openai.com/share/2dba769e-3ae2-4d4c-8c28-493dbd7bc6bd
#                               https://www.w3schools.com/python/python_conditions.asp
#                               https://github.com/codefellows/seattle-ops-301d10/tree/main/class-09/challenges




# Assign values to variables
a = 67
b = 76

# Original conditions
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
elif a < b:
    print("a is less than b")
elif a <= b:
    print("a is less than or equal to b")
elif a > b:
    print("a is greater than b")
elif a >= b:
    print("a is greater than or equal to b")
else:
    # Additional condition and action of your choice
    print("Some other condition is true")

    # New condition and action for both if and elif not being met
    if a % 2 == 0:
        print("a is an even number")
    else:
        print("a is an odd number")

# Stretch goals
# If statement with two conditions using 'and'
if a < b and a % 2 == 0:
    print("a is less than b and also an even number")

# If statement with two conditions using 'or'
if a > b or a % 2 != 0:
    print("Either a is greater than b or a is not an even number")

# Nested if statement
if a != b:
    print("a and b are not equal")
    
    if a > b:
        print("a is greater than b")
    else:
        print("a is less than or equal to b")

# If statement with 'pass' to avoid errors
if a == b:
    print("a and b are equal")
else:
    pass
