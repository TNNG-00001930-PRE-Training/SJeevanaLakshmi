"""5. Write a program that accepts a comma separated sequence of words as 
input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""

user_data = input("Enter sequence of words:") #user input from the consle
words = user_data.split(',') #split used to separate the words
s = words.sort()
for i in words:
    print(i,end=',') # sorted the given user_data and printed using , join

