"""3. Write a program that will print whether the number is a single digit number or double digit number or big number.
If given number is one digit number, print "Single digit number".If given number is two digit number, print "Double digit
number". If number is three digit number or bigger, print "Big number".
"""
num = int(input("Enter number:"))

if num >= 100:
    print("Big number")
elif num >= 10:
    print("Double digit number")
elif num >= 0:
    print("Single digit number")
else:
    print("Negative number")
