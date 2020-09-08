string_input = input()
letters = {}

for x in string_input:
    letters[x] = 1
if len(letters.values()) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')