"""
With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that
is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program: 8
"""
number_dic = {}
for i in range(1, int(input('pelse input a number >: '))+1):
    number_dic[i] = i*i
print(number_dic)