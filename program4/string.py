"""4. Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters"""

class String_upper(): #define a class
    
    def __init__(self): # define Init method
        self.u_str = " " # intiazed with an empty string
        
    def get_string(self): #created a method to get user input
        self.u_str =  input("Enter your string:")    #user input  

    def print_string(self): # created a method to print user input
        print(self.u_str.upper()) # Converted the input to upper case and printed

def testString(): # test method to check the class method
    teststring = String_upper() #created class object
    teststring.get_string() # calling get_string method
    teststring.print_string() # calling print_string method

testString()
