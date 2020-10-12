import sys


first_string = sys.stdin.readline().strip()
second_string = sys.stdin.readline().strip()

K, N = [int(ch) for ch in first_string.split(' ')]
cards = [int(ch) for ch in second_string.split(' ')]
# K, N = [4, 2]


# cards = [1,2,3,4,5,6,7,8,9,10]
# cards = [5, 10, 15, 20, 3, 6, 9, 25, 30, 12, 21, 24,]
# cards = [5, 3]


vasya = 0
petya = 0

for card in cards:
    if vasya >= K:
        print('Vasya')
        break
    elif petya >= K:
        print('Petya')
        break

    if card % 5 == 0 and card % 3 == 0:
        pass
    elif card % 5 == 0:
        vasya += 1
    elif card % 3 == 0:
        petya += 1
else:
    if petya == vasya:
        print('Draw')
    else:
        print('Vasya') if vasya > petya else print('Petya')

