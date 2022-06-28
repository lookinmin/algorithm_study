# LIS 골드5 전깃줄
# 2007 정보 올림피아드 초등부 4번
# a1 시작점 < a2시작점 -> a1의 끝점 > a2의 끝점 -> a1 삭제

# a 전봇대 기준 정렬 -> b 전봇대의 길이 - b 전봇대의 LIS길이 = 답

n = int(input())
a = []
b = []
dp = [0 for i in range(n)]
for i in range(n):
    a.append(list(map(int, input().split())))

a.sort(key=lambda x: x[0])
for i in range(n):
    b.append(a[i][1])

for i in range(n):
    for j in range(i):
        if b[i] > b[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(n-max(dp))

