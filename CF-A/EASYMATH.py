import math


def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1
    return lcm


quantity = int(input())

for i in range(quantity):
    data = input().split(' ')
    data = [int(item) for item in data]
    a = data[2]
    d = data[3]
    counter = 0
    list = [a, a + d, a + 2 * d, a + 3 * d, a + 4 * d]
    lcms = []
    print(math.floor(data[1] / a) - math.floor((data[0]-1) / a))
    print(math.floor(data[1] / (a + d)) - math.floor((data[0]-1) / (a + d)))
    print(math.floor(data[1] / (a + (2 * d))) - math.floor((data[0]-1) / (a + (2 * d))))
    print(math.floor(data[1] / (a + (3 * d))) - math.floor((data[0]-1) / (a + (3 * d))))
    print(math.floor(data[1] / (a + (4 * d))) - math.floor((data[0]-1) / (a + (4 * d))))
    counter += math.floor(data[1] / a) - math.floor((data[0]-1) / a)
    counter += math.floor(data[1] / (a + d)) - math.floor((data[0]-1) / (a + d))
    counter += math.floor(data[1] / (a + (2 * d))) - math.floor((data[0]-1) / (a + (2 * d)))
    counter += math.floor(data[1] / (a + (3 * d))) - math.floor((data[0]-1) / (a + (3 * d)))
    counter += math.floor(data[1] / (a + (4 * d))) - math.floor((data[0]-1) / (a + (4 * d)))
    set_temp = []
    for x in list:
        for y in list:
            if x == y:
                continue
            else:
                temp = lcm(x, y)
                if temp <= data[1]:
                    if (x, y) not in set_temp and (y, x) not in set_temp:
                        print("x, y", x, y)
                        print(temp)
                        set_temp.append((x, y))
                        lcms.append(temp)
    n = data[1] + 1 - data[0]
    result = 0
    list = [6, 9, 12, 15]
    list2 = [36, 28, 76, 24, 126, 266]
    print(n, counter)
    print('n before', n - counter)
    print(lcms)
    for h in lcms:
        result += math.floor(data[1] / h) - math.floor((data[0] - 1) / h)
    print("result", n - counter + result)