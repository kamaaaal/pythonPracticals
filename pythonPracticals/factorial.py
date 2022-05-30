# factorial,recursion

def fact(num):
    if num < 1:
        return 'factorial not possible'
    elif num == 1:
        return num
    else :
        return num * fact(num -1)

#  print(fact(5))
# get user input for a number to calculate factorial
num = int(input('Enter a number: '))
print(fact(num))
