calories = input().split(' ')
movements = input()

counter = 0
for x in movements:
    counter += int(calories[int(x)-1])
print(counter)