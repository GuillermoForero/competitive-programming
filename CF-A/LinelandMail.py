import math

length = int(input())

data = input().split(' ')

data = [int(item) for item in data]

for i in range(length):
    big, small = 0, 99999999999999
    if i == 0:
        small = abs(data[i + 1] - data[i])
        big = abs(data[length - 1] - data[i])
    elif i == length - 1:
        small = abs(data[length - 2] - data[i])
        big = abs(data[0] - data[i])
    else:
        small = min(abs(data[i + 1] - data[i]), abs(data[i - 1] - data[i]))
        big =  max(abs(data[0] - data[i]), abs(data[length - 1] - data[i]))
    print(str(small) + ' ' + str(big))
