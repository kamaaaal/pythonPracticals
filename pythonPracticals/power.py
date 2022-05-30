# implement a class with power method

# create a class with class keyword
class myMath:
    def pow(value,exponent):
        return value ** exponent

# get user input of base and power value
base = float(input('Enter the base: '))
power = float(input('Enter the power: '))
print('result : ', myMath.pow(base,power))
