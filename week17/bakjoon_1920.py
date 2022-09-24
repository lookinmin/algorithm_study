#이분 탐색, 실버4, 수 찾기

from sys import stdin, stdout
n = stdin.readline()
a = sorted(map(int, stdin.readline().split()))
m = stdin.readline()
isIn = map(int, stdin.readline().split())

def binary(i, a, start, end):
    if start > end:
        return 0
    mid = (start + end)//2
    if i == a[mid]:
        return 1
    elif i < a[mid]:
        return binary(i, a, start, mid - 1)
    elif i > a[mid]:
        return binary(i, a, mid + 1, end)



for i in isIn:
    start = 0
    end = len(a) -1
    print(binary(i, a, start, end))

