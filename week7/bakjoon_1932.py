# Dynamic Programming 실버1 정수 삼각형

n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

# 각 라인의 가장 왼쪽, 오른쪽 = 바로 위 숫자 더해줌
# 나머지 = 왼쪽 대각선, 오른쪽 대각선 중 최댓값 선택

for i in range(1, n):
    for j in range(len(arr[i])):
        if j == 0:     #제일 왼쪽
            arr[i][j] = arr[i][j] + arr[i-1][j]
        elif j == len(arr[i])-1:   #제일 오른쪽
            arr[i][j] = arr[i][j] + arr[i-1][j-1]
        else:
            arr[i][j] = max(arr[i-1][j-1], arr[i-1][j]) + arr[i][j]

print(max(arr[n-1]))


