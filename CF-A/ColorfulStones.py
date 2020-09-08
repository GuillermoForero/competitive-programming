string_one = input()
instructions = input()
index = 0
for x in instructions:
    if x == string_one[index]:
        index += 1
    if index == len(string_one):
        break
print(index+1)