input()
birds = input().split(' ')
birds = [int(item) for item in birds]
times = int(input())
for x in range(times):
    shot = input().split(' ')
    wire = int(shot[0])
    bird = int(shot[1])
    if len(birds) == 1:
        birds[0] = 0
    elif wire == 1:
        birds[wire] += birds[wire-1] - bird
    elif wire == len(birds):
        birds[wire-2] += bird - 1
    else:
        birds[wire] += birds[wire-1] - bird
        birds[wire-2] += bird - 1
    birds[wire-1] = 0

for y in birds:
    print(y)