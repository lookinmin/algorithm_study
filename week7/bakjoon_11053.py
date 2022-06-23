# Dynamic Programming 실버2 LIS
# LIS는 O(n^2)의 시간 복잡도와 O(n log n)의 시간복잡도가 있음

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * len(arr)

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))
