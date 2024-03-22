"""7. Write a program, which will find all such numbers between 1000 and 3000 (both included) 
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
"""class evenNumber():
    def __init__(self,num1,num2):
        self.u_num1 = num1
        self.u_num2 = num2
    def findallvalue(self): # created a method
        num = []                  # intialized a list
        for i in range(u_num1,u_num2+1): # looping statement
            if i % 2 == 0:  #condition to print even number 
                num.append(i) #adding the True values to num
        return num"""
import re 
u_num1 = int(input("Enter a number: "))
u_num2 = int(input("Enter a number: "))
      
for i in range(u_num1,u_num2):
  if re.search(r'^[02468]+$', str(i)):
        print(str(i),end=" ")



"""e = evenNumber(u_num1,u_num2)
out = e.findallvalue()
print(','.join(map(str,out)))"""
