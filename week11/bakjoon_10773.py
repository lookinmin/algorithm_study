# 스택 실버4 제로
# 가장 최근에 쓴 수 지우기

k = int(input())
stack = []
for i in range(k):
    a = int(input())
    if a == 0:
        stack.pop()
    else:
        stack.append(a)

print(sum(stack))
