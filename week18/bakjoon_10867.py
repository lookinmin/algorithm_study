#정렬, 실버5, 중복빼고 정렬

N = int(input())
arr = set(map(int, input().split()))
arr = list(arr)
arr.sort()
print(*arr)