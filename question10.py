"""
Write a program that accepts a sequence of whitespace separated words as input and prints the words after
 removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:
"""

a = input().split(' ')
a = sorted(list(set(a)))
print(' '.join(a))