input_text = input()
counter = 0
for x in input_text:
    if x.isupper():
        counter = counter+1
if counter > len(input_text)/2:
    print(input_text.upper())
else:
    print(input_text.lower())