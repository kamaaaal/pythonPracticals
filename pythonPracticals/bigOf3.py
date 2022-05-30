# big of 3

# define a function with three parametes(a,b,c)
# the function cheks whether a is greater than b and c
# else checks wheteher b is greater than a and c
# else checks whether c is greater than a and b

def bigOf3(a,b,c):
    if a > b:
        if a > c:
            print('value a: ',a,'is greater than b and c')
        else:
            print('value c: ',c,'is greater than a and b')
    elif b > c:
         print('value b: ',b,'is greater than a and c')
    else :
        print('value c: ',c,'is greater than a and b')

# get uset input using input() function
# split the number from user .split() method
# pass the number to bigOf3 function after converting them to integer using int() function

numbers = input('enter three numbers: ')
a,b,c = numbers.split()
bigOf3(int(a),int(b),int(c))
