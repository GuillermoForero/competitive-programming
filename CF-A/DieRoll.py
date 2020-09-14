from fractions import Fraction
numbers = input().split(' ')
numbers = [int(item) for item in numbers]
maximum = max(numbers)
var = 6-maximum +1
result = Fraction(str(var) +'/' + str(6))
if result==1:
    print('1/1')
elif result==0:
    print('0/1')
else:
    print(result)