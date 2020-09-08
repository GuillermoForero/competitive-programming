string_input = input()

list_of_ascii = [ord(c) for c in string_input]
list_of_ascii.insert(0, ord('a'))
total = 0
target = list_of_ascii[0]
for x in range(1, len(list_of_ascii)):
    total += min(abs(target - list_of_ascii[x]), 26 - abs(target - list_of_ascii[x]))
    target = list_of_ascii[x]
print(total)
