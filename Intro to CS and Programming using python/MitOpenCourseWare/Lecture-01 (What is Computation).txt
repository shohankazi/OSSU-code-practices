# import random
# random_num = random.randint(16,272)
# print(random_num)

# Topics
""" 
1. Represent knowledge with data structures
2. Iteration and recursion as a computational metaphors
3. abstraction of procedures and data types 
4. Organize and modularize systems using object classes and methods
5. Different classes of algorithms, searching and sorting 
6. Complexity of algorithms
"""

# What does a computer do
""" 
1. Fundamentally:
    => Perform calculations a billion calculations per second!
    => Remembers results 100s of gigabytes of storage!
2. What kinds of calculations?
    => built-in to the language
    => ones that you define as the programmer
3. Computers only know what you tell them
"""
# Types of Knowledge
""" 
1. Declarative knowledge is statements of fact.
    => someone will win a google cardboard before class ends
2. Imperative knowledge is a recipe or "how-to"
    => students sign up at http://bit.ly/60001-raffle
    => Ana opens her IDE
    => Ana chooses a random num between 1st and nth responder
    => Ana finds the number in the responders sheet. Winner!
"""
# A numerical Example
""" 
1. Square root of a number x is y such that y*y = x
2. recipe for deducing square root of a number x (16)
    => Start with a guess, g
    => If g*g is close enough to x, stop and sat g is the answer
    => Otherwise make a new guess by averaging g and x/g 
    => Using the new guess, repeat process until close enough.
"""
# What is a recipe
""" 
1. sequence of simple steps
2. flow of control process that specifies when each step is executed
3. a means of determining when to stop

1+2+3 = an algorithm!
"""

# Computers are machines
""" 
1. How to capture a recipe in a mechanical process
2. fixed program computer => calculator
3. stored program computer => machine stores and executes instructions
"""
# Stored Program computer 
""" 
1. sequence of instructions stored inside computer 
    => built from predefined set of primitive instructions
        1) arithmetic logic unit(ALU)
        2) simple data
        3) moving data
2. Special program (interpreter) executes each instruction in order
    => use tests to change flow of control through sequence 
    => stop when done
"""
# Basic Primitives
""" 
1. Turing showed that you can compute anything using 6 primitives
2. modern programming languages have more convenient set of primitives
3. can abstract methods to create new primitives
4. anything computable in one language is computable in any other programming language
"""

# Creating Recipes
""" 
1. a programming language provides a set of primitive operations
2. expressions are complex but legal combinations of primitives in a programming language
3. expressions and computations have values and meanings in a programming language
"""
# Aspects of languages
""" 
1. Primitive constructs
    => English : words
    => programming language : numbers, strings, simple operators
2. syntax
    => English :"cat dog boy" -> not syntactically valid
                "cat hugs boy" -> syntactically valid
    => Programming language : "hi"5 -> not syntactically valid
                            3.2*5 -> syntactically valid
3. static semantics is which syntactically valid strings have meaning
    => English: "I are hungry" -> syntactically valid but static semantic error
                3+"hi" -> static semantic error
4. semantics is the meaning associated with a syntactically correct string of symbols with no static semantic errors
    => English : can have many meanings "Flying planes can be dangerous"
    => programming languages: have only one meaning but may not be what programmer intended
"""
# Where things go wrong 
""" 
1. syntactic errors
    => common and easily caught
2. static semantic errors
    => some languages check for these before running program 
    => can cause unpredictable behavior 
3. no semantic errors but different meaning than what programmer intended 
    => program crashes, stops running
    => program runs forever
    => program gives an answer but different than expected
"""
# Python programs
""" 
1. a program is a sequence of definitions and commands 
    => definitions evaluated
2. commands (statements) instruct interpret to do something
3. can be typed directly in a shell or stored in a file that is read into the shell and evaluated
    => problem set 0 will introduce you to these in Anaconda
"""

# Objects
""" 
1. program manipulate data objects
2. objects have a type that defines the kinds of things programs can do to them
    => Ana is a human so she can walk, speak English, etc.
    => Chewbacca is a wookie so he can walk, "mwaaarhrhh", etc.
3. Objects are 
    => scalar (cannot be subdivided)
    => non-scalar (have internal structure that can be accessed)
"""
# Scalar Objects
""" 
1. int - represent integers, ex. 5
2. float - represent real numbers, ex. 3.27
3. bool - represent Boolean values True and False
4. NoneType - special and has one value, None
5. can use Type() to see the type of an object
""" 
# Type Conversions (CAST)
""" 
1. can convert object of one type to another 
2. float(3) converts integer 3 to float 3.0
3. int (3.9) truncates float 3.9 to integer 3
"""
# Printing to Console
""" 
to show output from code to a user, use print command
"""
# Operators ON ints and floats
""" 
1. i + j -> the sum
2. i - j -> the difference
3. i * j -> the product
4. i / j -> division 
5. i % j -> the remainder when i is divided by j
6. i**j  -> i to the power of j
"""

# Binding Variables and Values
""" 
1. equal sign is an assignment of a value to a variable name
    pi = 3.1416
    pi_approx = 22/7
2. value stored in computer memory
3. an assignment binds names to value
4. retrieve value associated with name or variable by invoking the name, by typing pi
"""
# Abstracting Expressions
""" 
1. why give names to values of expressions? 
2. to reuse names instead of values
3. easier to change code later
    pi = 3.1416
    radius = 2.2
    area = pi*(radius**2)
"""
# Programming vs Math
""" 
1. in programming, you do not "solve for x"
    pi = 3.1416
    radius = 2.2
    # area of circle
    area = pi * (radius ** 2)
    radius = radius + 1
"""
# Changing Bindings 
""" 
1. can re-bind variable names using new assignment statements
2. previous value may still stored in memory but lost the handle for it
3. value for area does not change until you tell the computer to do the calculation again
    pi = 3.1416
    radius = 2.2
    area = pi * (radius ** 2)
    radius = radius + 1
"""
usa_gold = 46
uk_gold = 27
romania_gold = 1
total_gold = usa_gold + uk_gold + romania_gold
print(total_gold)
romania_gold += 1
print(total_gold)