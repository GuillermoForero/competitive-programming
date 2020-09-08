number_of_problems = int(input())
result = 0
for n in range(number_of_problems):
    decisions = input().split(' ')
    if decisions.count('1') >= 2:
        result = result + 1
print(result)