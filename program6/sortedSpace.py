"""6. Write a program that accepts a sequence of whitespace separated 
words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
"""
user_data = input("Enter sequence of words:") #user input from the consle
words = user_data.split(' ') #split used to separate the words with space
sort = set(words) # set does't allows duplicate
print(' '.join(sorted(sort))) # sorted the given user_data and printed using , join
