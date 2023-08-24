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