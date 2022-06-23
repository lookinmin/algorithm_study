# Dynamic Programming 골드5 LCS

import sys
read = sys.stdin.readline

str1 = read().strip()
str2 = read().strip()

dp = [0] * len(str2)

for i in range(len(str1)):
    cnt = 0
    for j in range(len(str2)):
        if cnt < dp[j]:
            cnt = dp[j]
        elif str1[i] == str2[j]:
            dp[j] = cnt+1

print(max(dp))