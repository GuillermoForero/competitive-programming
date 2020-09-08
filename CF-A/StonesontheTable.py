input()

stones = input()
counter = 0
temp_stone = stones[0]
for x in range(1, len(stones)):
    if stones[x] == temp_stone:
        counter += 1
    else:
        temp_stone = stones[x]
print(counter)