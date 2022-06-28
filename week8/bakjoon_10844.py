# Dynamic Programming 실버 1 쉬운 계단 수
# 길이가 N인 계단 수의 총 갯수, 계단 수 = 인접한 모든 자리 차이가 1인 수 ex)45656
n = int(input())

dp = [[0 for i in range(10)]for j in range(101)]
# 자리수에 따른 이차원 배열

for i in range(1, 10):
    dp[1][i] = 1
# 자리수가 1인 경우, 계단수는 1 이므로 1~9까지 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:          # 맨뒤에 0인 경우, 10일때
            dp[i][j] = dp[i-1][1]
        elif j == 9:        # 맨뒤에 9인 경우, 89일때
            dp[i][j] = dp[i-1][8]
        else:               # 맨뒤가 0, 9가 아닌 경우, 대각선 위 위치의 숫자들
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % 1000000000)