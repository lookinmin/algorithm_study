# 스택 큐 , 실버3, 쇠막대기
# 정올 초등부3번, 중등부 2번

stick = list(input())
stack = []
cnt = 0

for i in range(len(stick)):
    if stick[i] == "(":
        stack.append("(")
    else:
        if stick[i-1] == "(":
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1

print(cnt)