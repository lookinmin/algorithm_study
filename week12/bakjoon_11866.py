# 큐, 덱 실버5 유세푸스 문제0

n, k = map(int, input().split())
q = []
arr = []
for i in range(n):
    q.append(int(i+1))

print("<", end="")

while q:
    for i in range(k-1):
        q.append(q[0])
        q.pop(0)
    print(q.pop(0), end="")
    if q:
        print(", ", end="")
print(">")

