operations = input().split('+')
operations = [int(item) for item in operations]
operations.sort()

if len(operations) == 1:
    print(operations[0])
else:
    result = ''
    for x in operations:
        result += str(x) + '+'
    print(result[0:len(result)-1])