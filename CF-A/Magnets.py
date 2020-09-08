number_of = int(input())

count_of_groups = 0
numb_temp = '0'
for i in range(number_of):
    input_temp = input()
    if not (numb_temp == input_temp):
        count_of_groups += 1
        numb_temp = input_temp
print(count_of_groups)