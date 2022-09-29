#구현, 브론즈1, 쉽게 푸는 문제

from sys import stdin
a, b = map(int, stdin.readline().strip().split())
arr = [0]
for i in range(1,b+1):
    for j in range(i):
        arr.append(i)

print(sum(arr[a:b+1]))