# print pattern

#get user input to get the range of the pattern
ran = int(input('Enter the range: '))

for i in range(1,ran+1):
    print('*' * i)
    if i == ran:
        for y in range(i,0,-1):
            print('*'*y)
