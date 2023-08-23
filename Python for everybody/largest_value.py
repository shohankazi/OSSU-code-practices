# Finding the largest value

largest = 0
print('Before',largest)
for num in [9,41,12,3,74,15] :
    if num > largest :
        largest = num
    print(largest,num)
print('After',largest)