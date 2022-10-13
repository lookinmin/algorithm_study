# 정렬, 실버5, 배열 합치기

N, M = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

res = arr1 + arr2
res.sort()
print(*res)