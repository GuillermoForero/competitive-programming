input()
cards = input().split(' ')
cards = list(map(int, cards))

sereja, dima = 0, 0
turn_of = True
while len(cards) > 0:
    left_card = cards[0]
    right_card = cards[len(cards) - 1]
    if turn_of:
        if left_card > right_card:
            sereja += cards.pop(0)
        else:
            sereja += cards.pop(len(cards) - 1)
        turn_of = False
    else:
        if left_card > right_card:
            dima += cards.pop(0)
        else:
            dima += cards.pop(len(cards) - 1)
        turn_of = True
print(sereja, dima)