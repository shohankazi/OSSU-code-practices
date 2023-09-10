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
# Comparison Example
""" 
pset_time = 15
sleep_time = 8
print(sleep_time > pset_time)
derive = True
drink = False
both = drink and derive
print(both) 
"""
# Control Flow Branching
""" 
1. <condition> has a value True or False
2. evaluate expressions in that block if <condition> is True
"""
# Indentation

""" 
1. matters in Python
2. how you denote blocks of code
    
    x = float(input("Enter a number for x: "))
    y = float(input("Enter a number for y: "))
    if x == y:
        print("x and y are equal")
        if y != 0:
            print("therefore, x / y is", x/y)
    elif x < y:
    print("x is smaller")
    else:
        print("y is smaller")
    print("thanks!") 
"""

# = vs ==
""" 
x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))
if x == y:
        print("x and y are equal")
        if y != 0:
            print("therefore, x/y is",x/y)
elif x < y:
        print("x is smaller")
else:
        print("y is smaller")
print("thanks!")
"""
# Control Flow: while loops
""" 
while <execution>:
    <expression>
    <expression>
    ...
1. <condition> evaluates to a boolean
2. if <condition> is True, do all the steps inside the while code block
3. check <condition> again
4. repeat until <condition> is False
"""
# While loop examples
""" 
program:
n = input("You're in the lost Forest. Go left or right?")
while n == "right":
    n = input("You're in the Lost Forest. Go left or right? ")
print("You got out of the Lost Forest!")
"""
# CONTROL FLOW: while and for LOOPS
""" 
iterate through numbers in a sequence
==> more complicated with while loop
n = 0
while n < 5:
    print(n)
    n = n+1
==> shortcut with for loop
for n in range(5):
    print(n)
"""
# CONTROL FLOW: for LOOPS
""" 
for <variable> in range(<some_num>):
    <expression>
    <expression>
    ... 

1. each time through the loop, <variable> takes a value
2. first time, <variable> starts at the smallest value
3. next time, <variable> gets the prev value + 1
4. etc.
"""
# range(start,stop,step)
""" 
1. default values are start = 0 and step = 1 and optional
2. loop until value is stop - 1  

my_sum = 0
for i in range(7, 10):
    my_sum += i
print(my_sum)
my_sum = 0
for i in range(5, 11, 2):
    my_sum += i
print(my_sum)
"""
# break STATEMENT
""" 
1. immediately exits whatever loop it is in
2. skips remaining expressions in code block
3. exits only innermost loop! 
====> with while loop <====
while <condition_1>:
    while <condition_2>:
        <expression_a>
        break
        <expression_b>
    <expression_c>
    
====> with for loop <====
my_sum = 0
for i in range(5, 11, 2):
    my_sum += i
    if my_sum == 5:
        break
        my_sum += 1
print(my_sum)
"""
# for VS while LOOPS
# for loops
""" 
1. know number of iterations
2. can end early via break
3. uses a counter
4. can rewrite a for loop using a while loop
"""
# while loops 
""" 
1. unbounded number of iterations
2. can end early via break
3. can use a counter but must initialize before loop and increment it inside loop
4. may not be able to rewrite a while loop using a for loop 
"""