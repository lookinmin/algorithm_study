# Dynamic Programming 실버1 RGB거리
# 집을 칠하는 비용의 최솟값
# 연속하는 집의 색은 같지 않아야 한다

# 모르겠음 나중에 다시


n = int(input())
dp = []
for i in range(n):
    dp.append(list(map(int,input().split())))

for i in range(1, len(dp)):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + dp[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + dp[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + dp[i][2]

print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))

