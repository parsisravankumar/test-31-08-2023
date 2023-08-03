"""2. Write a program to check if a word is present in the given string. For example, if the word 'orange' is present
in the "This is orange juice".
"""
string = str(input("enter the string: "))
word = str(input("enter the word: "))

if word in string:
    print(f"{word} is present in the given string")
else:
    print(f"{word} is not present in  the given string")