# 스택 실버4 균형잡힌 세상
# 다시 한번 풀기

while 1:
    s = input()
    if s == ".":
        break
    stack = []
    temp = True
    for i in s:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if not stack or stack[-1] == "[":       # not stack ??
                temp = False
                break
            elif stack[-1] == "(":
                stack.pop()
        elif i == "]":
            if not stack or stack[-1] == "(":
                temp = False
                break
            elif stack[-1] == "[":
                stack.pop()
    if temp == True and not stack:
        print("yes")
    else:
        print("no")
