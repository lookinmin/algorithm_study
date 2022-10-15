# 구현, 브론즈1, 부녀회장이 될테야

# 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.

from sys import stdin
T = int(stdin.readline())
for _ in range(T):
    k = int(stdin.readline())
    n = int(stdin.readline())
    people = [i for i in range(1, n + 1)]
    for i in range(k):
        new = []
        for j in range(n):
           new.append(sum(people[:j+1]))
        people = new.copy()
    print(people[-1])