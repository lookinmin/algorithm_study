# 스택 실버2 스택 수열

# push를 오름차순으로 할 때,
# 입력과 같은 수열을 만들기 위한 연산
# 모르겠음 다시

n = int(input())

arr = []
stack = []
cnt = 1
temp = True

for i in range(n):
    num = int(input())
    while cnt <= num:
        arr.append(cnt)
        stack.append("+")
        cnt += 1
    if arr[-1] == num:
        arr.pop()
        stack.append("-")
    else:
        temp = False

if temp == False:
    print("NO")
else:
    for i in stack:
        print(i)
