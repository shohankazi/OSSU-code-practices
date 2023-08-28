# Tuples are like lists
""" Tuples are another kind of sequence that functions much like a list - they have elements which are indexed starting at 0 """

# x = ('Glenn','Sally','Joseph')
# print(x[2])
# y = (1,9,2)
# print(y)
# print(max(y))
# for iter in y :
#     print(iter)

# But Tuples are "immutable"

""" Unlike a list, once you create a tuple, you cannot alter its contents - similar to a string """

# x = [9,8,7]
# x[2] = 6
# print(x)
# y = 'ABC'
# y[2] = 'D'
# print(y) # TypeError: 'str' object does not support item assignment

# z = (5,4,3)
# z[2] = 0
# print(z) TypeError: 'str' object does not support item assignment

# Things not to do with tuples
""" x = (3,2,1)
x.sort()
x.append()
x.reverse() """
# These things we can't do into tuples

# A Tale of TWO Sequences

""" l = list()
dir(1)

t = tuple()
dir(t)
"""

# Tuples are more efficient 

""" 
1. Since Python does not have to build tuple structures to be modifiable, they are simpler and more efficient in terms of memory use and performance than lists.
2. So in our program when we are making "temporary variables" we prefer tuples over lists.
"""

# Tuples and Assignment 

""" 
1. We can also put a tuple on the left-hand side of an assignment statement.
2. We can even omit the parentheses.
"""

# (x,y) = (4,'fred')
# print(x)

# (a,b) = (99,98)
# print(a)

# Tuples and Dictionaries
""" The items() method in dictionaries returns a list of (key,value) tuples """

# d = dict()
# d['csev'] = 2
# d['cwen'] = 4
# for (k,v) in d.items() :
#     print(k,v)
# tups = d.items()
# print(tups)

# Tuples are Comparable
""" The comparison operator work with tuples and other sequences. If the first item is equal,Python goes on to the next element, and so on, until it finds elements that differ """

# (0,1,2) < (5,1,2)
# (0,1,2000000) < (0,3,4)
# ('Jones','Sally') < ('Jones','Sam')
# ('Jones','Sally') > ('Adams','Sam')


# Practice Set

""" fname = input('Enter file: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand :
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w,0) + 1
# print(di)

# x = sorted(di.items()) 
# print(x,'\n')
# print(x[:5])

temp = list()
for k,v in di.items() :
    # print(k,v)
    new_tuple = (v,k)
    temp.append(new_tuple)
# print('flipped',temp)

temp = sorted(temp, reverse=True)
print('sorted', temp[:5])

for v,k in temp[:5]:
    print(k,v) 
"""
    
# Exercise 10.2

""" 
fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
hand = open(fname)
di = dict()
for lin in hand :
    if lin.startswith('From '):
        wds = lin.split()
        for w in wds[5:6]:
            time = w.split(':')
            for hour in time[:1]:
                di[hour] = di.get(hour,0) + 1
                
for k,v in sorted(di.items()) :
    print(k,v) 
"""

    
    
days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])
    
    
    
#     new_tuple = (k,v)
#     temp.append(new_tuple)
# print(sorted(temp))


        # print(wds)
#         lin = lin.rstrip()
#         wds = lin.split()
#         for w in wds:
#             di[w] = di.get(w,0) + 1
# # print(di)

# temp = list()
# for k,v in di.items() :
#     print(k,v)
#     new_tuple = (v,k)
#     temp.append(new_tuple)
# # print('flipped',temp)


