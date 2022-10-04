# 구현, 실버4, 카드1

n = int(input())

card = [i for i in range(1, n+1)]

while len(card) != 1:
    print(card[0], end=" ")
    card.pop(0)
    a = card.pop(0)
    card.append(a)

print(card[0])