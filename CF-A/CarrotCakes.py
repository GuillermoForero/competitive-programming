import math

variables = input().split(' ')

variables = [int(item) for item in variables]

without_second_oven = math.ceil(variables[0] / variables[2]) * variables[1]

t = variables[2] / variables[1]
libre1, libre2 = 0, variables[3]
isLibre1, isLibre2 = False, False
counter = 999999999999999
n = variables[0]
for x in range(1, without_second_oven + 1):
    if libre1 == 0:
        if n > 0:
            n -= variables[2]
            libre1 = libre1 + variables[1]
        else:
            isLibre1 = True
    if libre2 == 0:
        if n > 0:
            n -= variables[2]
            libre2 = variables[1]
        else:
            isLibre2 = True
    libre1 -= 1
    libre2 -= 1
    if isLibre1 and isLibre2:
        break
    counter = x

if without_second_oven <= counter:
    print('NO')
else:
    print('YES')