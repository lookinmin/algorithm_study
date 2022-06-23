#Dynamic Programming 실버2 연속합

n = int(input())

arr = list(map(int, input().split()))

dp = [0] * len(arr)                             #입력받은 수열의 크기 만큼의 리스트 선언

dp[0] = arr[0]                                  #0번째 인덱스는 입력한 수열과 동일

for i in range(1, len(arr)):
    dp[i] = max(arr[i], dp[i-1] + arr[i])       #리스트의 인덱스를 합의 최댓값으로 치환

print(max(dp))                                  #치환된 리스트의 인덱스들 중 가장 큰 값 출력