# Greedy, 실버2, A->B
# A to B : (1) x2, (2) append 1

from sys import stdin

a, b = map(int, input().split())
r = 1
while b != a:
    r += 1
    temp = b
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2

    if temp == b:
        print(-1)
        break
else:
    print(r)
