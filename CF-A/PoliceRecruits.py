input()

array_input = input().split(' ')
counter_of_coops = 0
crimes_not_resolve = 0
for x in array_input:
    value = int(x)
    if value > 0:
        counter_of_coops += value
    elif counter_of_coops > 0:
        temporal = counter_of_coops - abs(value)
        if temporal >= 0:
            counter_of_coops -= abs(value)
        else:
            value += counter_of_coops
            counter_of_coops = 0
            crimes_not_resolve += abs(value)
    else:
        crimes_not_resolve += abs(value)
print(crimes_not_resolve)