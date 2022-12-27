# DP, 실버3, 이친수

from sys import stdin

n = int(stdin.readline())

s = [0,1,1]

for i in range(3, 91):
    s.append(s[i-2] + s[i-1])

print(s[n])

