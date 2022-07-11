# 큐와 덱, 골드5, AC
# 정수 배열 연산, Reverse, Discard

# 나중에 다시


from collections import deque
import sys

t = int(input())

for i in range(t):
    func = sys.stdin.readline().rstrip()
    n = int(input())
    num = sys.stdin.readline().rstrip()[1:-1].split(",")     # 대괄호, 쉼표 버리고 숫자만
    deq = deque(num)

    rev, front, back = 0, 0, len(deq)-1
    flag = 0
    if n == 0:
        deq = []
        front, back = 0, 0

    for j in func:
        if j == "R":
            rev += 1
        elif j == "D":
            if len(deq) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev % 2 == 0:
                    deq.popleft()
                else:
                    deq.pop()
    if flag == 0:
        if rev % 2 == 0:
            print("[" + ",".join(deq) + "]")
        else:
            deq.reverse()
            print("[" + ",".join(deq) + "]")


