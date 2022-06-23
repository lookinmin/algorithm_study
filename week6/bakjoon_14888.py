#Sw 소프트웨어 역량 1번, 실버1
import sys

input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))

maximum = -1e9
minimum = 1e9

def dfs(depth, sum, p, m, g, d):
    global maximum, minimum
    if depth == n:
        maximum = max(sum, maximum)
        minimum = min(sum, minimum)
        return

    if p:
        dfs(depth + 1, sum + num[depth], p - 1, m, g, d)
    if m:
        dfs(depth + 1, sum - num[depth], p, m-1, g, d)
    if g:
        dfs(depth + 1, sum * num[depth], p, m, g-1, d)
    if d:
        dfs(depth + 1, int(sum/num[depth]), p, m, g, d-1)

dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)