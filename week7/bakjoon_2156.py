# Dynamic Programming 실버1 포도주 시식

n = int(input())
wine = [0]
for i in range(n):
    wine.append(int(input()))

dp = [0]
dp.append(wine[1])

if n > 1:
    dp.append(wine[1] + wine[2])
for i in range(3, n+1):
    dp.append(max(dp[i-1], dp[i-3] + wine[i-1] + wine[i], dp[i-2] + wine[i]))

print(dp[n])

# 궁금증 : 왜 [0]으로 시작하면 오류 없고, []로 시작하면 오류임? 시발?

