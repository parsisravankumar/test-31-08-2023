"""8. Write a program to display the elements of list thrice if it is a number and display the 
element terminated with ‘#’ if it is not a number. 
For example, if the content of list is [‘41’, ‘DHRUVA’, ‘GURU’, ‘13’, ‘ZARA’]
The output should be
414141
DHRUVA#
GURU#
131313
ZARA#"""

input_list = ['41', 'DHRUVA', 'GURU', '13', 'ZARA']
output = ""

for i in input_list:
    if i.isdigit() == True:
        output += i * 3
    elif i.isalpha() == True:
        output += i+"#"
        
print(output)