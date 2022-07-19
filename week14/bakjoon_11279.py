# 우선순위 큐 실버2 최대 힙

# n = int(input())
#
# arr = []
# for i in range(n):
#     x = int(input())
#     if x > 0:
#         arr.append(x)
#     elif x == 0:
#         if len(arr) == 0:
#             print(0)
#         else:
#             print(max(arr))
#             arr.remove(max(arr))

# 답은 맞았지만 시간초과 발생

import heapq
from sys import stdin

n = int(stdin.readline())
heap = []

for i in range(n):
    x = int(stdin.readline())
    if x == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, [-x, x])