#이분탐색, 실버5, 숫자카드

n = int(input())
card = list(map(int, input().split()))
m = int(input())
num = list(map(int, input().split()))

card.sort()     #이분탐색은 정렬이 선행

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

for i in range(m):
    if binarySearch(card, num[i],0, n-1) is not None:
        print(1, end = " ")
    else:
        print(0, end = " ")