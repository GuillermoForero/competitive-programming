input()
rows = input().split(' ')
for x in range(len(rows)):
    rows[x] = int(rows[x])
rows.sort()
for i in rows:
    print(i)
