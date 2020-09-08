array_of_values = input().split(' ')
for x in range(1, 11):
    if (int(array_of_values[0]) * x) % 10 == 0 or (int(array_of_values[0]) * x) % 10 == int(array_of_values[1]):
        print(x)
        break
