a, b = input().split(' ')
a = int(a)
b = int(b)
year = 0
while a<=b:
    a = a*3
    b = b*2
    year = year + 1
print(year)