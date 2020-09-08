number_of_teams = input()

array_of_teams = []
counter = 0
for x in range(int(number_of_teams)):
    array_of_teams.append(input().split(' '))

for x in range(len(array_of_teams)):
    for n in range(len(array_of_teams)):
        if x == n:
            continue
        if array_of_teams[x][0] == array_of_teams[n][1]:
            counter += 1
print(counter)