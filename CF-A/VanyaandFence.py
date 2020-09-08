max_height = int(input().split(' ')[1])

persons = input().split(' ')
result = 0
for x in persons:
    if int(x) > max_height:
        result = result+2
    else:
        result = result+1
print(result)