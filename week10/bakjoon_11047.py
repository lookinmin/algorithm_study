# 그리디 알고리즘 실버4 동전 0
# 큰 동전이 작은 동전의 배수이다 -> 그리디 알고리즘 사용

n, k = map(int, input().split())
arr = []
cnt = 0
for i in range(n):
    arr.append(int(input()))

for i in range(n-1, -1, -1):
    cnt += k // arr[i]      # cnt값 = k를 동전으로 나눈 몫의 합
    k = k % arr[i]          # k는 나머지로 계속 나눠주면서 반복

print(cnt)


