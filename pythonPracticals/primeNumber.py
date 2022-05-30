#print prime numbers less than given input

# get user inout for the range
ran = int(input('enter the range : '))

for i in range(2,ran+1):
    count = 0
    for y in range(2,i//2+1):
        if i%y == 0:
            count += 1
    if count == 0:
        print(i,' is a prime number') 
