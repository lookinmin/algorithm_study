# DP, 실버3, 1,2,3더하기

from sys import stdin

t = int(stdin.readline())

def sol(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return sol(n-1) + sol(n-2)+sol(n-3)
# f(n) = f(n-1) + f(n-2) + f(n-3) -> 규칙 찾기

for i in range(t):
    n = int(stdin.readline())
    print(sol(n))
