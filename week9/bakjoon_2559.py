# 누적합 실버3 수열
# 정보 올림피아드 2011 초등부 1번

n, k = map(int, input().split())
arr = list(map(int, input().split()))

part = sum(arr[:k])         #k개의 합을 이미 정하고
result = [part]

for i in range(0, len(arr)-k):          #이미 정한 k개의 합에서 맨 앞의 값을 제하고 맨 뒤에값 추가
   part = part - arr[i] + arr[i+k]
   result.append(part)

print(max(result))
