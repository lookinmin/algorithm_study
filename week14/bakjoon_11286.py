# 우선순위큐 실버1 절댓값 힙

import heapq
from sys import stdin

# n = int(stdin.readline())
# heap1 = []
# heap2 = []
#
# for i in range(n):
#     x = int(stdin.readline())
#
#     if x == 0:
#         if len(heap1) + len(heap2) == 0:
#             print(0)
#         else:
#             if abs(heap1[0]) >= abs(heap2[0]):
#                 print(heapq.heappop(heap2))
#             elif abs(heap1[0]) < abs(heap2[0]):
#                 print(heapq.heappop(heap1))
#             elif len(heap1) == 0 and heap2:
#                 print(heapq.heappop(heap2))
#             elif len(heap2) == 0 and heap1:
#                 print(heapq.heappop(heap1))
#     else:
#         if x > 0:
#             heapq.heappush(heap1, x)
#         elif x < 0:
#             heapq.heappush(heap2, x)

# 배열 2개 사용 -> 런타임에러

n = int(stdin.readline())
heap = []

for i in range(n):
    x = int(stdin.readline())
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)