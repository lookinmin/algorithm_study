# 스택 골드4 오큰수
# 오큰수 (NGE) : 오른쪽에 있는 수 중에서 Ai보다 크면서 가장 왼쪽에 있는 수
# 이중 빈복문 -> 시간초과
# 나중에 다시

n = int(input())
arr = list(map(int, input().split()))

ans = [-1] * n
stack = []

stack.append(0)

for i in range(1, n):
    while stack and arr[stack[-1]] < arr[i]:
        ans[stack.pop()] = arr[i]
    stack.append(i)

print(*ans)