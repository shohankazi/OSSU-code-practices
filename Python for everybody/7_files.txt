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

# fhand = open('mbox-short.txt')
# for line in fhand :
#     if line.startswith("From:") :
#         print(line)
        
# bad file names 
""" fname = input('Enter the filename: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ',fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence: '):
        text = line
        count = count + 1
        i_pos = text.find(':')
        extracted_value = text[i_pos+1:]
        space_cleared = extracted_value.strip()
        new_number = float(space_cleared)
        total = 0.0
        total = total + new_number
        avg_number = total / count
print('Average spam confidence: ',avg_number,count)
 """
fname = input("Enter file name: ")
fhand = open(fname)

try:
    fhand = open(fname)
except:
    print('File cannot be opened: ',fname)
    quit()
count = 0
val = 0

for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count += 1
    line_strip = line.rstrip()
    at_pos = line_strip.find(' ')
    f_num = float(line[at_pos:])
    val += f_num
print(f"Average spam confidence: {val/count}")

# Summary

""" 
1.  Secondary Shortage
2.  Opening a file - file handle
3.  File structure - newline character
4.  Reading a file line by line with a for loop
5.  Searching for lines
6.  Reading file names
7.  Dealing with bad files
"""