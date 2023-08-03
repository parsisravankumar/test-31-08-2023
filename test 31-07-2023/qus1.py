"""1. Write a program to print a string formed with the first 2 and the last 2 characters of the given string.
 Assume the size of given string is always greater than or equal to 4."""

input_str = input("Enter a string (at least 4 characters): ")

if len(input_str) >= 4:
    first_two_chars = input_str[:2]
    last_two_chars = input_str[-2:]
    result = first_two_chars + last_two_chars
    print("Result:", result)
else:
    print("Error: The input string should have at least 4 characters.")