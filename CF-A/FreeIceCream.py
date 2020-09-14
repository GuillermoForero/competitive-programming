start = input().split(' ')
number_of_ice_creams = int(start[1])
sad_kids = 0
for x in range(int(start[0])):
    arrive = input().split(' ')
    number_of = int(arrive[1])
    if arrive[0] == '+':
        number_of_ice_creams += number_of
    else:
        if number_of_ice_creams >= number_of:
            number_of_ice_creams -= number_of
        else:
            sad_kids += 1
print(number_of_ice_creams, sad_kids)