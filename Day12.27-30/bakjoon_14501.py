# DP, 실버3, 퇴사

from sys import stdin
n = int(input())

schedule = [list(map(int, stdin.readline().split()))for i in range(n)]
dp = [0 for j in range(n+1)]

for i in range(n):
    for j in range(i + schedule[i][0], n+1):
        if dp[j] < dp[i] + schedule[i][1]:
            dp[j] = dp[i] + schedule[i][1]

print(dp[-1])