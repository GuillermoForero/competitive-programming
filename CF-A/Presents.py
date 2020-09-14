input()

iths = input().split(' ')

iths = [int(item) for item in iths]
list_final = {}

for x in range(len(iths)):
    list_final[iths[x]] = (x + 1)
result = ''
for y in range(1, len(iths) + 1):
    result += str((list_final[y]))
    if y < len(iths):
        result += ' '
print(result)