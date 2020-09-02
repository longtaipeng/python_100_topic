"""
Write a program that accepts sequence of lines as input and prints the lines after making all characters
 in the sentence capitalized.
Suppose the following input is supplied to the program:
"""

lst = []

while True:
    a = input()
    if len(a) == 0:
        break
    lst.append(a)

for i in lst:
    print(i.upper())