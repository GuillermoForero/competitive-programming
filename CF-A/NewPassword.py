from random import randint

data = input().split(' ')
long = int(data[0])
different = int(data[1])
possibilities = []
while len(possibilities) < different:
    var = chr(randint(97, 122))
    if possibilities.count(var) == 0:
        possibilities.append(var)
result = ''
while len(result) < long:
    for x in possibilities:
        if len(result) >= long:
            break
        result += x
print(result)