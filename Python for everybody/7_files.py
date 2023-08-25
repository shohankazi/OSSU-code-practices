# File handle as a sequence

""" 
A file handle open for read can be treated as a sequence of strings where each line in the file is a string in the sequence.
We can use the for statement to iterate through a sequence.
Remember - a sequence is an ordered set.
"""
# xfile = open('mbox.txt')
# for cheese in xfile:
#     print(cheese)

# Counting lines in a file
""" 
Open a file read-only.
Use a for loop to read each line.
Count the lines and print out the number of lines.
"""
# fhand = open('mbox.txt')
# count = 0
# for line in fhand :
#     count = count + 1
# print('Line count: ', count)

# Reading the whole file

""" 
We can read the whole file(newlines and all) into a single string
"""
# fhand = open('mbox-short.txt')
# inp = fhand.read()
# print(len(inp))
# print(inp[:20])

# Searching through a file

""" 
We can put an if statement in our for loop to only print lines that meet some criteria.
"""

fhand = open('mbox-short.txt')
for line in fhand :
    if line.startswith("From:") :
        print(line)
        