for row_item in range(5):
    row = input().split(' ')
    if row.count('1') > 0:
        column_item = row.index('1')
        print(abs(3 - (int(column_item)+1)) + abs(3 - (row_item+1)))