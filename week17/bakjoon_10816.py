#이분탐색, 실버4, 숫자카드 2

from sys import stdin
n = stdin.readline()
got = sorted(map(int, stdin.readline().split()))
m = stdin.readline()
card = map(int, stdin.readline().split())

def binary(a, arr, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if a == arr[mid]:
        return arr[start: end + 1].count(a)
    elif a < arr[mid]:
        return binary(a, arr, start, mid - 1)
    elif a > arr[mid]:
        return binary(a, arr, mid + 1, end)

card_dic = {}

for i in got:
    start = 0
    end = len(got)-1
    if i not in card_dic:
        card_dic[i] = binary(i, got, start, end)

print(' '.join(str(card_dic[x]) if x in card_dic else '0' for x in card ))