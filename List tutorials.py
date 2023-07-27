# 1
# Create a Python script that removes all the occurrences of a given element of a list.
x=[1,2,3,3,4,4,5,8,7,12,12]
x1=12
while x1 in x:
    x.remove(x1)
print(x)

# 2
# Create a Python script that removes all the elements of a list that are duplicates.
w=[1,2,3,3,4,4,5,8,7,12,12]
z=[]
for item in w:
    if item not in z:
        z.append(item)
print(z)

# 3
# Consider the following string: nums = '10,20,30,40,50'
# Create a Python script that creates a list of integers from the string.
# The resulting list will be: [10, 20, 30, 40, 50]
number='10,20,30,40,50'
n= number.split(',')
print(n)

# 4
# Write a Python script that finds all numbers that are divisible by 7 but are not a multiple of 5, between 1500 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence (CSV) on a single line.
x=[]
for n in range(1500,3201):
    if n%7==0 and n%5!=0:
        x.append(str(n))
print(',' .join(x))

# 5
# Write a program that prompts the user for a long string containing multiple words separated
# by whitespaces and prints back the same string with the words in backward order.
# For example, say I type the string: My name is Andrei
# Then the script should print out: Andrei is name My
x= input('enter a string:')
y= x.split(' ')
x_reversed= ' '.join(reversed(y))
print(x_reversed)

# 6
# Write a Python program that accepts a hyphen-separated sequence of words as input and
# prints the words in a hyphen-separated sequence after sorting them alphabetically.
# Sample input string : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow
x=input('enter a word:')
y=x.split('-')
z= sorted(y)
s='-'.join(z)
print(s)

# 7
# Write a Python program that accepts as input a sequence of words separated by one
# or more whitespaces and prints out the same words with the letters in reversed order. Do not use list comprehension.
# Sample input string: I love cat and dogs
# Expected Result: I evol tac dna sgod
x=input('enter a word:')
y= x.split()
s=0
for n in y:
    y[s]=n[::-1]
    s+=1
new=' '.join(y)
print(new)

# 8
# Create an alternative solution for the previous challenge using list comprehension.
x=input('enter a word:')
string= x.split( )
word_reverse= [word[::-1] for word in string]
new_string=' '.join(word_reverse)
print (new_string)

# 9
# Create a Python script that calculates and displays the number of occurrences of each element of a list.
# Sample list: list('mamma mia mm')
# Expected Result:
# m ---> 6
# a ---> 3
# ---> 2
# i ---> 1
v=list('daddy is the best of all father')
word_list=list()
for letter in set(v):
    number= v.count(letter)
    word_list.append((letter, number))
word_list.sort(key=lambda x:x[1], reverse=True)
for letter in word_list:
    print(f'{letter[0]}    {letter[1]}')

# 10
# Consider a list of words(strings). Write a Python script that generates a list of tuples where
# the first element of the tuple is the word in the list and the second element is its length.
# Use list comprehension if possible.
# Sample List: words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
my_list = ['Junior', 'Clovis', 'Manu']
words_number = [(word, len(word)) for word in my_list]
print(words_number)