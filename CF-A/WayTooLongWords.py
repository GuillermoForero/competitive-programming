number_of_words = int(input())

for x in range(number_of_words):
    word = input()
    if len(word) > 10:
        print(word[0] + str(len(word) - 2) + word[len(word) - 1])
    else:
        print(word)