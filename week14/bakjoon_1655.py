# 우선순위 큐 골드2 가운데를 말해요
# 다시 풀기

from sys import stdin
import heapq

n = int(stdin.readline())
heap1 = []
heap2 = []

for i in range(n):
    x = int(stdin.readline())
    if len(heap1) == len(heap2):
        heapq.heappush(heap1, -x)
    else:
        heapq.heappush(heap2, x)

    if heap2 and heap2[0] < -heap1[0]:
        lv = heapq.heappop(heap1)
        rv = heapq.heappop(heap2)

        heapq.heappush(heap1, -rv)
        heapq.heappush(heap2, -lv)

    print(-heap1[0])