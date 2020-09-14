while True:
    input1 = ''
    try:
        input1 = input().split(' ')
    except EOFError:
        pass
    if not input1 or len(input1) == 0:
        break
    step, mod = int(input1[0]), int(input1[1])
    list_set = set()
    before = 0
    list_set.add(0)
    while True:
        before = (before + step) % mod
        if before in list_set:
            break
        list_set.add(before)
    print_result = ''
    for x in range(0, 10 - len(input1[0])):
        print_result += ' '
    print_result += input1[0]
    for x in range(0, 10 - len(input1[1])):
        print_result += ' '
    print_result += input1[1]
    print_result += '    '
    if len(list_set) == mod:
        print_result += 'Good Choice'
    else:
        print_result += 'Bad Choice'
    print(print_result)
    print()
