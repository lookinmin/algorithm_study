# Dynamic Programming 실버3 계단오르기
# 1칸 or 2칸 가능
# 연속된 3칸 불가능, 마지막은 무조건

n = int(input())
stair = [0 for i in range(301)]
#for i in range(n):
#    stair.append(int(input()))    -> 이렇게 했을 때 런타임 에러
# dp = [0] * len(stair)

dp = [0 for i in range(301)]
for i in range(n):
    stair[i] = int(input())

dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = max(stair[1] + stair[2], stair[0] + stair[2])

for i in range(3, n):
    dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])
# 마지막 전 계단을 밟은 경우 vs 밟지 않은 경우

print(dp[n-1])