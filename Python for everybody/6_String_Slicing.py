# Slicing Strings
# We can also look at any continuous section of a string using a colon operator
# The second number is one beyond the end of the slice "up to but not including"
# If the second number is beyond the end of the string, it stops at the end

""" 
str = 'Monty Python'
print(str[0:4])
print(str[6:7])
print(str[6:20]) 
"""

# Eliminating
""" 
print(str[:2])
print(str[8:])
print(str[:]) 
"""

# String Concatenation
# When the + operator is applied to strings, it means "Concatenation"

""" a = 'Hello'
b = a + 'There'
print(b)
c = a + ' ' + 'There'
print(c) """

# Using in as a logical operator
# The in keyword_has can also be used to check to see if one string is "in" another string
# The in expression is a logical expression that returns True or False and can be used in an if statement

""" 
fruit = "banana"
print('n' in fruit)
print('m' in fruit)
print('nan' in fruit)
if 'a' in fruit :
    print('Found it!') 
"""

# String Comparison
""" 
word_has = 'banana'
if word_has == 'banana' :
    print('All right, bananas,')
if word_has < 'banana' :
    print('Your word_has,' + word_has + ', comes after banana.')
elif word_has > 'banana' :
    print('Your word_has,' + word_has + ', comes after banana.')
else: 
    print('All right, bananas.') 
"""
    
# String Library

""" 
Python has a number of string functions which are in the string library.
These functions are already built into every string - we invoke them by appending the function to the string variable. 
These functions do not modify the original string, instead they return a new string that has been altered.
"""
# greet = 'Hello bob'
# zap = greet.lower()
# print(zap)
# print(greet)
# print('Hi there'.lower())

# stuff = 'Hello world'
# print(type(stuff))
# print(dir(stuff))

# String Library

""" str.capitalize()
str.center()
str.endswith()
str.find()
str.lstrip()
str.replace()
str.lower()
str.rstrip()
str.strip()
str.upper() """

# Searching a string
""" 
We use the find() function to search for a substring within another string.
find() finds the occurrence of the substring.
If the substring is not found, find() returns -1
Remember that string position starts at 0.
"""
# fruit = 'banana'
# pos = fruit.find('na')
# print(pos)
# aa = fruit.find('z')
# print(aa)

# make everything UPPERCASE
""" 
You can make a copy of a string in lower case or upper case.
Often when we are searching for a string using find() we first convert the string to lower case so we can search a string regardless of case.
"""

""" 
greet = 'Hello Bob'
nnn = greet.upper()
print(nnn)
www = greet.lower()
print(www) 
"""

# Search and replace

""" 
The replace() function is like a "search and replace" operation in a word processor.
It replaces all occurrences of the search string with the replacement string.
"""
# greet = 'Hello Bob'
# nstr = greet.replace('Bob','Jane')
# print(nstr)
# nstr = greet.replace('o','x')
# print(nstr)

# Stripping Whitespace
""" 
Sometimes we want to take a string and remove whitespace at the beginning and/or end.
lstrip() and rstrip()remove whitespace at the left or right.
strip() removes both beginning and ending whitespace.
"""

greet = '   Hello Bob   '
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())
# greet.rstrip()
# print(greet)
# greet.strip()
# print(greet)