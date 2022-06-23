# Dynamic Programming 골드3 가장 긴 바이토닉 부분 수열

n = int(input())
arr = list(map(int, input().split()))

dp1 = [0] * len(arr)
dp2 = [0] * len(arr)
dp3 = [0] * len(arr)

for i in range(n):              #증가하는 수열중 가장 긴거
    for j in range(i):
        if arr[i] > arr[j] and dp1[i] < dp1[j]:
            dp1[i] = dp1[j]
    dp1[i] += 1


for i in range(n-1, -1, -1):    #감소하는 수열 중 가장 긴거
    for j in range(n-1, i, -1):
        if arr[i] > arr[j] and dp2[i] < dp2[j]:
            dp2[i] = dp2[j]
    dp2[i] += 1


for i in range(n):              #같은 인덱스 넘버의 두 수열의 길이 더하기 -1(원소 중복)
    dp3[i] = dp1[i] + dp2[i] - 1

print(max(dp3))