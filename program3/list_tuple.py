"""3. Write a program which accepts a sequence of comma-separated numbers 
from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""
# takin the input from the user
user_input = input("Enter sequence of numbers:").split(',')
print(user_input) # results a list
print(tuple(user_input)) # by type conversion results a tuple