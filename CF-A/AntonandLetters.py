input_array = input().replace('{', '').replace('}', '').replace(' ', '').split(",")
counter_set = {}
for x in input_array:
    if x == '':
        break
    counter_set[x] = 1
print(len(counter_set))