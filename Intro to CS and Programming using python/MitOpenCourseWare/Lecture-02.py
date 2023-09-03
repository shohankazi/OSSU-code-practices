""" 
====>> Important Lessons <<====
1. By definition of the input command, python always make it a string. If you want to work with number, you have to explicitly tell it I'm going to work with number
2. If I use comma(,), it will automatically add space. But if I do it with (+) operator i have to give a space explicitly.
"""
# Strings
""" 
1. letters, special characters, spaces, digits
2. enclose in quotation marks or single quotes
    hi = "hello there"
3. concatenate strings
    name = "ana"
    greet = hi + name
    greeting = hi + " " + name
4. do some operations on a string as defined in python docs 
    silly = hi + " " + name * 3
"""

# Input/Output : print
""" 
1. used to output stuff to console
2. keyword is print
    x = 1
    print(x)
    x_str = str(x)
    print("my fav num is",x,".","x =",x)
    print("my fav num is " + x_str + ". " + "x = " + x_str)
"""
# Input/Output : input("")
""" 
1. Prints whatever is in the quotes
2. user types in something and hits enter
3. binds that value to a variable
    text = input("Type anything")
    print(5*text)
4. input gives you a string so must cast if working with numbers
    num = int(input("Type a number..."))
    print(5*num)
"""
# Comparison operators On int,float,string
""" 
1. i and j are variable names
2. comparisons below evaluate to a boolean
    i > j
    i >= j
    i < j
    i <= j
    i == j -> equality test, True if i is the same as j
    i != j -> inequality test, True if i not the same as j
"""
# Logic operators on bools
""" 
1. a and b are variable names (with Boolean values)
not a -> True if a is False
a and b -> True if both are True
a or b -> True if either or both are True
"""