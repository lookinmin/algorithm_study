# Dynamic Programming, 실버3 1로만들기

n = int(input())
dp = [0] * (n+1)    # 게산된 값 미리 저장

# 내생각 : 3으로 나눌 수 없을 때까지 나눈다 -> 2가 나올때 까지 나눈다 -> 1을 뺀다 <- 그리디 였음

# def makeOne(n):
#     cnt = 1
#     while n % 3 == 0:
#         n / 3
#         cnt += 1
#
#     while (n != 2 and n % 2 == 0):
#         n / 2
#         cnt += 1
#
#     if(n == 2):
#         print(cnt)
#
#
# print(makeOne(n))

# 이거 아니였고

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)        # 계산된 횟수를 저장하므로 +1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[n])
