"""
Write a program that accepts a comma separated sequence of words as input and prints the words in
 a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
"""

world_list = input().split(',')
world_list.sort()
print(','.join(world_list))