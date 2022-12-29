# Greedy, 실버5, 수들의 합
# N개의 자연수의 합 = S, N의 최대값?

S = int(input())
n = 1
while n*(n+1) / 2 <= S:
    n += 1

print(n-1)
