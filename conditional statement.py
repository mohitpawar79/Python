"""
if
if-else
if-elif-else
"""

"""
if syntax

if condition:
    statements
"""
# Example

age = input("Enter Your age : ")
if int(age) >= 18:
    print("You'r 18+ ")

"""
if else syntax

if condition:
    statement
else:
    statement
"""
#  Example

if int(age) >= 18:
    print("You'r 18+ ")
else:
    print("You'r 18-")

"""
if - elif Syntax

if condition:
    statement
elif condition:
    statement
else:
    statement
    
"""

# example

if int(age) >=45:
    print("ypou are 45 + ")
elif int(age) >= 18:
    print("You are 18+ ")
else:
    print("You are 18-")
