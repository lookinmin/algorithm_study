# Dynamic Programming 실버3 파도반 수열
# 1 -> 1 -> 1 -> 2 -> 2 -> 3 -> 4 -> 5 ->7 -> 9
# 나선에서 가장 긴 변의 길이의 삼각형 추가
t = int(input())

dp = [0] * 101
dp[0], dp[1], dp[2] = 1, 1, 1
dp[3], dp[4] = 2, 2
for i in range(5, 100):
    dp[i] = dp[i-1] + dp[i-5]

for i in range(t):
    n = int(input())
    print(dp[n-1])