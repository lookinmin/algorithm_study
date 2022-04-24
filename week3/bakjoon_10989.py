#오름차순 정렬 실버5

import sys

n = int(sys.stdin.readline())           #시간제합 5초로 인해 빠른 입력
arr = [0]*10001

for i in range(n):
    arr[int(sys.stdin.readline())] += 1

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)

