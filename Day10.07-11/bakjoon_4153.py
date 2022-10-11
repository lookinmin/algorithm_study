# 기하, 브론즈3, 직각삼각형
from sys import stdin
while True:
    arr = list(map(int, stdin.readline().split()))
    if arr[0] == arr[1] == arr[2] == 0:
        break
    else:
        arr.sort(reverse=True)
        if arr[0]**2 == arr[1]**2 + arr[2]**2:
            print("right")
        else:
            print("wrong")