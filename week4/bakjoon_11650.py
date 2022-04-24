#정렬 6번, 실버5

n = int(input())

arr = []
for i in range(n):
    x, y = map(int, input().split())  # 좌표 2차원 리스트로 입력
    arr.append([x, y])  # y기준 정렬이므로 y,x 순으로 append

arr.sort()

for x, y in arr:
    print(x, y)
