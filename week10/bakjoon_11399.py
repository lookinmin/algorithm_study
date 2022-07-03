# 그리디 알고리즘 실버4 ATM
# 돈 인출에 최소걸리게

n = int(input())
p = list(map(int, input().split()))
k = 0
p.sort()
arr = []
for i in range(n):
    k += p[i]
    arr.append(k)

print(sum(arr))
