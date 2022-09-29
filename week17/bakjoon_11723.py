# 구현, 실버5, 집합

from sys import stdin
m = int(stdin.readline())
sarr = set()

for _ in range(m):
    temp = stdin.readline().strip().split()

    if len(temp) == 1:
        if temp[0] == "all":
            sarr = set([i for i in range(1, 21)])
        elif temp[0] == "empty":
            sarr = set()

    else:
        ctr, n = temp[0], temp[1]
        n = int(n)
        if ctr == "add":
            sarr.add(n)
        elif ctr == "remove":
            sarr.discard(n)
        elif ctr == "check":
            if n in sarr:
                print(1)
            else:
                print(0)
        elif ctr == "toggle":
            if n in sarr:
                sarr.discard(n)
            else:
                sarr.add(n)
