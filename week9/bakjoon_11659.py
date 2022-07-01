# 누적합 실버3 구간 합 구하기 4

import sys

input = sys.stdin.readline

# 위에 두 줄 없으면 시간초과

n, m = map(int, input().split())

arr = list(map(int, input().split()))

dp = [0] * (n+1)
for i in range(n):
    dp[i+1] = dp[i] + arr[i]    # 구간 누적합


for i in range(m):
    a, b = map(int, input().split())
    print(dp[b] - dp[a-1])