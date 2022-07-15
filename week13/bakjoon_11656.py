# 문자열, 실버4, 접미사 배열

s = str(input())
stack = []
for i in s:
    stack.append(s)
    s = s[1:]

for i in sorted(stack):
    print(i)
