#구현, 브론즈3, 윷놀이

from sys import stdin
for i in range(3):
    arr = list(map(int, stdin.readline().split()))

    if sum(arr) == 0:
        print("D")
    elif sum(arr) == 1:
        print("C")
    elif sum(arr) == 2:
        print("B")
    elif sum(arr) == 3:
        print("A")
    else:
        print("E")
