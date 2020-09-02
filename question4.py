"""
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a 
tuple which contains every number.Suppose the following input is supplied to the program:
"""

num_str = input('pelse input > ')
num_list = num_str.split(',')
num_tuple = tuple(num_list)
print(num_list)
print(num_tuple)   