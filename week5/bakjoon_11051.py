#이항계수2, 실버1

from math import factorial

n, k = map(int, input().split())

result = factorial(n) // (factorial(k) * factorial(n - k))
print(result % 10007)