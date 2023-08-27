# What is a collection?
""" 
1. A collection is nice because we can put more than one value in it and carry them all around in one convenient package.
2. We have a bunch of values in a single "variable"
3. We do this by having more than one place "in" the variable
4. We have ways of finding the different places in the variable.
"""
# A story of two collections
""" 
1. List = A linear collection of values that stay in order
2. Dictionary = A "bag" of values, each with it's own label.
"""
# Dictionaries
""" 
1. Dictionaries are Python's most powerful data collection
2. Dictionaries allow us to do fast database-like operations in Python
3. Dictionaries have different names in different languages.
    ==> Associative Arrays - Perl/PHP
    ==> Properties or Map or HashMap - Java
    ==> Property Bag - C# / .Net
    ==> Objects - Javascript
4. Lists index their entries based on the position in the list
5. Dictionaries are like bags - no order
6. So we index the things we put in the dictionary with a "lookup tag"
"""
# purse = dict()
# purse['money'] = 12
# purse['candy'] = 3
# purse['tissues'] = 75
# print(purse)

# Comparing Lists and dictionaries
""" Dictionaries are like lists except that they use keys instead of numbers to look up values """
# list
    # lst = list()
    # lst.append(21)
    # lst.append(183)
    # print(lst)
    # lst[0] = 23
    # print(lst)
# Dictionaries
    # ddd = dict()
    # ddd['age'] = 21
    # ddd['course'] = 182
    # print(ddd)
    # ddd['age'] = 23
    # print(ddd)

""" 
        List
    Key ---- Value
    [0] ---- 21
    [1] ---- 183
        Dictionary
    Key ------------ Value
    ['course] ----   182
    ['age]    ----   21
"""

# Dictionary Literals
""" 
1. Dictionary literals use curly braces and have a list of key:value pairs
2. You can make an empty dictionary using empty curly braces.
"""
# jjj = {'chuck': 1, 'fred': 42,'jan':100}
# print(jjj)
# ooo = { }
# print(ooo)

# Many counters with dictionary
""" One common use of dictionaries is counting how often we "see" something """

# ccc = dict()
# ccc['csev'] = 1
# ccc['cwen'] = 1
# print(ccc)
# ccc['cwen'] = ccc['cwen'] + 1
# print(ccc)

# Dictionary Tracebacks
"""
1. It is an error to reference a key which is not in the dictionary.
2. We can use the in operator to see if a key is in the dictionary. 
"""
# ccc = dict()
# print(ccc['csev'])
# print('csev' in ccc)

# When we see a new name
""" 
When we encounter a new name, we need to add a new entry in the dictionary and if the second or later time we have seen the name, we simply add one to the count in the dictionary under that name.
"""
# counts = dict()
# names = ['csev','cwen','csev','zqian','cwen']
# for name in names :
#     if name not in counts:
#         counts[name] = 1
#         # print(counts)
#     else:
#         counts[name] = counts[name] + 1
# print(counts)

# The get method for dictionaries
""" The pattern of checking to see if a key is already in a dictionary and assuming a default value if the key is not there is so common that there is a method called get() that does this for us. Default value if key does not exist(and no traceback)"""

# if name in counts:
#     x = counts[name]
# else :
#     x = 0
# x = counts.get(name,0)
# print(x)

# Simplified counting with get()
""" We can use get() and provide a default value of zero when the key is not yet in the dictionary - and then just add one """

# counts = dict()
# names = ['csev','cwen','csev','zqian','cwen']
# for name in names :
#     counts[name] = counts.get(name,0) + 1
# print(counts)

# Counting Pattern

""" The general pattern to count the words in a line of text is to split the line into words, then loop through the words and use a dictionary to track the count of each word independently. """

# counts = dict()
# print('Enter a line of text: ')
# line = input('')
# words = line.split()
# print('Words:',words)
# print('Counting...')
# for word in words:
#     counts[word] = counts.get(word,0) + 1
# print('Counts',counts)

# Definite loops and dictionaries
""" Even though dictionaries are not stored in order, we can write a for loop that goes through all the entries in a dictionary - actually it goes through all of the keys in the dictionary and looks up the values. """

# counts = {'chuck':1,'fred':42,'jan':100}
# for key in counts:
#     print(key,counts[key])

# Retrieving lists of Keys and Values

# jjj = {'chuck':1,'fred':42,'jan':100}
# # print(jjj)
# print(jjj.keys())
# print(jjj.values())
# print(jjj.items())

# Bonus: Two Iteration Variables
""" 
1. We loop through the key-value pairs in a dictionary using two iteration values
2. Each iteration, the first variable is the key and the second variable is the corresponding value for the key.
"""
# jjj = {'chuck':1,'fred':42,'jan':100}
# for k,v in jjj.items():
#     print(k,v)

name = input('Enter File:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigCount = None
bigWord = None
for word,count in counts.items():
    if bigCount is None or count > bigCount:
        bigWord = word
        bigCount = count
print(bigWord,bigCount)
