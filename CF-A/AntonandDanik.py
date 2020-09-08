input()
string_input = input()

anton, danik = string_input.count('A'), string_input.count('D')
if anton > danik:
    print('Anton')
elif anton < danik:
    print('Danik')
else:
    print('Friendship')