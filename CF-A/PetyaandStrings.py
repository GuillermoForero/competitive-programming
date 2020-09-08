first_string = input()
second_string = input()

first_string = first_string.lower()
second_string = second_string.lower()
if first_string > second_string:
    print(1)
elif first_string < second_string:
    print(-1)
else:
    print(0)