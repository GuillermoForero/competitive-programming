input()
kids = input().replace(' ', '')
teams = 0
results = []
while True:
    if "1" in kids and "2" in kids and "3" in kids:
        teams += 1
        string_results = str(kids.find('1') + 1) + ' '
        string_results += str(kids.find('2') + 1) + ' '
        string_results += str(kids.find('3') + 1)
        kids = kids.replace('1', '0', 1).replace('2', '0', 1).replace('3', '0', 1)
        results.append(string_results)
    else:
        break
print(teams)
for x in results:
    print(x)
