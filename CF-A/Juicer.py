data = input().split(' ')
data = [int(item) for item in data]
sizes = input().split(' ')
sizes = [int(item) for item in sizes]
waste = 0
entero1 = 2
entero2 = 5
resultado = entero1/entero2
counter_waste = 0
for item in range(len(sizes)):
    if sizes[item] <= data[1]:
        if sizes[item] + waste > data[2]:
            counter_waste += 1
            waste = 0
        else:
            waste += sizes[item]
print(counter_waste)