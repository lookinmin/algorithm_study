# 큐와 덱, 실버4, 덱
# 덱은 무엇인가? -> 양방향 큐

from collections import deque
import sys

n = int(input())
deq = deque()

for i in range(n):
    arr = sys.stdin.readline().split()
    if arr[0] == "push_front":
        deq.appendleft(arr[1])
    elif arr[0] == "push_back":
        deq.append(arr[1])
    elif arr[0] == "pop_front":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    elif arr[0] == "pop_back":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    elif arr[0] == "size":
        print(len(deq))
    elif arr[0] == "empty":
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif arr[0] == "front":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif arr[0] == "back":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[len(deq)-1])