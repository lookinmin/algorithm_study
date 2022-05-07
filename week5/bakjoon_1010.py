#다리 놓기, 실버 5 = mCn

from math import factorial

t = int(input())

for i in range(t):
    n, m = list(map(int, input().split()))
    num = factorial(m) // (factorial(n) * factorial(m - n))
    print(num)