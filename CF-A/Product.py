while True:
    input1 = ''
    input2 = ''
    try:
        input1 = input()
        input2 = input()
    except EOFError:
        pass
    if not input1 or not input2:
        break
    print(int(input1) * int(input2))