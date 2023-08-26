# Programming

# Algorithm
""" A set of rules or steps used to solve a problem. """
# Data Structure 
""" A particular way of organizing data in a computer """

# What is not a collection 
""" Most of our variables have one value in them -when we put a new value in the variable, the old value is overwritten """
# x = 2
# x = 4
# print(x)

# A list is a kind of a collection
""" 
1. A collection allows us to put many values in a single "Variable".
2. A collection is nice because we can carry all many values around in one convenient package.
"""
# friends = ['Joseph', 'Glenn', 'Sally']
# carryon = ['socks','shirt','perfume']
# print(friends)
# print(carryon)

# List Constants
""" 
1. List constants are surrounded by square brackets and the elements in the list are separated by commas.
2. A list element can be any python object - even another list.
3. A list can be empty.
"""
# print([1,24,76])
# print(['red','yellow','blue'])
# print(['red',24,98.6])
# print(1,[5,6],7)
# print([])

# list = [5,3,4,5,6]
# for i in list :
    # print(i)
    
""" Looking inside lists """
# friends = ['Joseph', 'Glenn', 'Sally']
# for friend in friends :
#     print('Happy birthday: ',friend)
# for friend in friends :
#     print('Happy new year: ',friend[0])

# Lists are mutable(Changeable)
""" 
1. Strings are "immutable = unchangeable" - we cannot change the contents of a string - we must make a new string to make any change.
2. Lists are "mutable = Changeable" - we can change an element of a list using the index operator.
"""
fruit = 'Banana'
# fruit[0] = 'b'
# print(fruit) # it will show traceback error.

x = fruit.lower()
print(x)
lotto = [2,14,26,41,68]
lotto[2] = 28
print(lotto)
