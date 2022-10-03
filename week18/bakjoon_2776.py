# 이분탐색, 실버4, 암기왕

from sys import stdin

T = int(stdin.readline())


def binarySearch(arr, target, start, end):
    while start <= end:
        mid = (start+end)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for _ in range(T):
    N = int(stdin.readline())
    one = list(map(int, stdin.readline().split()))
    M = int(stdin.readline())
    two = list(map(int, stdin.readline().split()))

    one.sort()
    for i in two:
        if binarySearch(one, i, 0, N-1) is not None:
            print(1)
        else:
            print(0)
