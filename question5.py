"""
Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
"""

class Input_Outstring():

    def get_String(self):
        self.str = input('pelse input > ')

    def print_String(self):
        print('{}'.format(self.str.upper()))


ss = Input_Outstring()
ss.get_String()
ss.print_String()