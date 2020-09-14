import math

quantity = int(input())

for i in range(quantity):
    data = input().split(' ')
    data = [int(item) for item in data]
    a = data[2]
    d = data[3]
    counter = 0
    if a % d == 0 or d % a == 0:
        counter += data[1] - math.floor(data[1] / a)
    else:
        counter += math.floor(data[1] / a) - math.floor(data[0] / a)
        counter += math.floor(data[1] / (a + d)) - math.floor(data[0] / (a + d))
        counter += math.floor(data[1] / (a + 2 * d)) - math.floor(data[0] / (a + 2 * d))
        counter += math.floor(data[1] / (a + 3 * d)) - math.floor(data[0] / (a + 3 * d))
        counter += math.floor(data[1] / (a + 4 * d)) - math.floor(data[0] / (a + 4 * d))
    print(counter)