"""8. Write a program that accepts a sentence and 
calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9"""
import string
class upper_lower():

    def __init__(self,str):
        self.u_str = str
    def countn(self):
        upper = 0
        lower = 0
        for char in self.u_str:
            if char.isupper():
                upper += 1
            elif char.islower():
                lower += 1
        return upper, lower
    
u_str = input("Enter a string:")
tocall = upper_lower(u_str)
res = tocall.countn()
print("UPPER CASE:",res[0])
print("LOWER CASE:",res[1])