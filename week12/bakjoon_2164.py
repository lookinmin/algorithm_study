# 큐, 덱 실버4 카드2

import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque([])

for i in range(n):
    q.append(int(i+1))

while len(q) > 1:
    q.popleft()
    a = q.popleft()
    q.append(a)

print(*q)

