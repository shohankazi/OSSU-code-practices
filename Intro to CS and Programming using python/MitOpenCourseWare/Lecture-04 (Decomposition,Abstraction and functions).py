# HOW DO WE WRITE CODE?
""" 
1. so far…
    • covered language mechanisms
    • know how to write different files for each computation
    • each file is some piece of code
    • each code is a sequence of instructions
2. problems with this approach
    • easy for small-scale problems
    • messy for larger problems
    • hard to keep track of details
    • how do you know the right info is supplied to the right part of code
"""

# GOOD PROGRAMMING

""" 1. more code not necessarily a good thing
2. measure good programmers by the amount of functionality
3. introduce functions
4. mechanism to achieve decomposition and abstraction """

# EXAMPLE – PROJECTOR

""" 1. a projector is a black box
2. don't know how it works
3. know the interface: input/output
4. connect any electronic to it that can communicate with that input
5. black box somehow converts image from input source to a wall, magnifying it
6. ABSTRACTION IDEA: do not need to know how projector works to use it 
7. projecting large image for Olympics decomposed into separate tasks for separate projectors
8. each projector takes input and produces separate output
9. all projectors work together to produce larger image
10. DECOMPOSITION IDEA: different devices work together to achieve an end goal
"""

# CREATE STRUCTURE with DECOMPOSITION
""" 
1. in projector example, separate devices
2. in programming, divide code into modules
    • are self-contained
    • used to break up code
    • intended to be reusable
    • keep code organized
    • keep code coherent
3. this lecture, achieve decomposition with functions
4. in a few weeks, achieve decomposition with classes 
"""
# SUPRESS DETAILS with ABSTRACTION
""" 
1. in projector example, instructions for how to use it are sufficient, no need to know how to build one
2. in programming, think of a piece of code as a black box
    • cannot see details
    • do not need to see details
    • do not want to see details
    • hide tedious coding details
3. achieve abstraction with function specifications or docstrings
"""
# FUNCTIONS
""" 
1. write reusable pieces/chunks of code, called functions
2. functions are not run in a program until they are “called” or “invoked” in a program
3. function characteristics:
    • has a name
    • has parameters (0 or more)
    • has a docstring (optional but recommended)
    • has a body
    • returns something 
"""
# VARIABLE SCOPE
""" 
1. formal parameter gets bound to the value of actual parameter when function is called
2. new scope/frame/environment created when enter a function
3. scope is mapping of names to objects 
def f( x ):
    x = x + 1
    print('in f(x): x =', x)
    return x
x = 3
z = f( x )
4. Python returns the value None, if no return given
5. represents the absence of a value
"""
# return vs. print
# return
""" 
1. return only has meaning inside a function
2. only one return executed inside a function
3. code inside function but after return statement not executed
4. has a value associated with it, given to function caller 
"""
# print
""" 
1. print can be used outside functions
2. can execute many print statements inside a function
3. code inside function can be executed after a print statement
4. has a value associated with it, outputted to the console 
"""
# FUNCTIONS AS ARGUMENTS
""" arguments can take on any type, even functions 
def func_a():
    print 'inside func_a'
def func_b(y):
    print 'inside func_b'
    return y
def func_c(z):
    print 'inside func_c'
    return z()
print func_a()
print 5 + func_b(2)
print func_c(func_a)
"""
# SCOPE EXAMPLE
""" 
1. inside a function, can access a variable defined outside
2. inside a function, cannot modify a variable defined outside -- can using global variables, but frowned upon
def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('g: x =', x)
    h()
    return x
x = 3
z = g(x)
"""
# DECOMPOSITION & ABSTRACTION
""" 
1. powerful together
2. code can be used many times but only has to be debugged once!
"""