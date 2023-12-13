# TUPLES, LISTS,ALIASING,MUTABILITY, CLONING
# TUPLES
""" 
1. an ordered sequence of elements, can mix element types
2. cannot change element values, immutable
3. represented with parentheses 
4. conveniently used to swap variable values
5. used to return more than one value from a function
te = ()
t = (2,"mit",3)
t[0] -> evaluates to 2
(2,"mit",3) + (5,6) -> evaluates to (2,"mit",3,5,6)
t[1:2] -> slice tuple, evaluates to ("mit",)
t[1:3] -> slice tuple, evaluates to ("mit",3)
len(t) -> evaluates to 3
t[1] = 4 -> gives error, can't modify object
"""
# LISTS
""" 
1. ordered sequence of information, accessible by index
2. a list is denoted by square brackets, []
3. a list contains elements
    • usually homogeneous (ie, all integers)
    • can contain mixed types (not common)
4. list elements can be changed so a list is mutable
"""
# INDICES AND ORDERING
""" 
a_list = []
L = [2, 'a', 4, [1,2]]
len(L) -> evaluates to 4
L[0] -> evaluates to 2
L[2]+1 -> evaluates to 5
L[3] -> evaluates to [1,2], another list!
L[4] -> gives an error
i = 2
L[i-1] -> evaluates to ‘a’ since L[1]='a' above
"""
# CHANGING ELEMENTS
""" 
1. lists are mutable!
2. assigning to an element at an index changes the value
L = [2, 1, 3]
L[1] = 5
3. L is now [2, 5, 3], note this is the same object L
"""
# ITERATING OVER A LIST
""" 
1. compute the sum of elements of a list
2. common pattern, iterate over list elements
total = 0
for i in range(len(L)):
    total += L[i]
print(total)
3. notice
• list elements are indexed 0 to len(L)-1
• range(n) goes from 0 to n-1 
"""
# OPERATIONS ON LISTS - ADD
""" 
1. add elements to end of list with L.append(element)
2. mutates the list!
L = [2,1,3]
L.append(5) -> L is now [2,1,3,5]
3. what is the dot?
    • lists are Python objects, everything in Python is an object
    • objects have data
    • objects have methods and functions
    • access this information by object_name.do_something()
    • will learn more about these later
4. to combine lists together use concatenation, + operator, to give you a new list
5. mutate list with L.extend(some_list)
L1 = [2,1,3]
L2 = [4,5,6]
L3 = L1 + L2 -> L3 is [2,1,3,4,5,6]
L1, L2 unchanged
L1.extend([0,6]) -> mutated L1 to [2,1,3,0,6]
"""
# OPERATIONS ON LISTS - REMOVE
""" 
1. delete element at a specific index with del(L[index])
2. remove element at end of list with L.pop(), returns the removed element
3. remove a specific element with L.remove(element)
    • looks for the element and removes it
    • if element occurs multiple times, removes first occurrence
    • if element not in list, gives an error
L = [2,1,3,6,3,7,0] # do below in order
L.remove(2) -> mutates L = [1,3,6,3,7,0]
L.remove(3) -> mutates L = [1,6,3,7,0]
del(L[1]) -> mutates L = [1,3,7,0]
L.pop() -> returns 0 and mutates L = [1,3,7] 
"""
# CONVERT LISTS TO STRINGS AND BACK
""" 
1. convert string to list with list(s), returns a list with every character from s an element in L
2. can use s.split(), to split a string on a character parameter, splits on spaces if called without a parameter
3. use ''.join(L) to turn a list of characters into a string, can give a character in quotes to add char between every element
s = "I<3 cs" -> s is a string
list(s) -> returns ['I','<','3',' ','c','s']
s.split('<') -> returns ['I', '3 cs']
L = ['a','b','c'] -> L is a list
''.join(L) -> returns "abc"
'_'.join(L) -> returns "a_b_c"
"""
# OTHER LIST OPERATIONS
""" 
1. sort() and sorted()
2. reverse() and many more! 
L=[9,6,0,3]
sorted(L) -> returns sorted list, does not mutate L
L.sort() -> mutates L=[0,3,6,9]
L.reverse() -> mutates L=[9,6,3,0] 
"""
# LISTS IN MEMORY
""" 
1. lists are mutable
2. behave differently than immutable types
3. is an object in memory
4. variable name points to object
5. any variable pointing to that object is affected
6. key phrase to keep in mind when working with lists is side effects
"""
# ALIASES
""" 
1. hot is an alias for warm – changing one changes the
other!
2. append() has a side effect 
"""
# CLONING A LIST
""" 
1. create a new list and copy every element using chill = cool[:]
"""
# SORTING LISTS
""" 
1. calling sort() mutates the list, returns nothing
2. calling sorted() does not mutate list, must assign result to a variable
"""
# LISTS OF LISTS OF LISTS OF….
""" 
1. can have nested lists
2. side effects still possible after mutation
"""
