# 구현, 브론즈3, 지능형 기차
from sys import stdin
result = 0
max_result = 0
for i in range(4):
    out, on = map(int, stdin.readline().split())
    result -= out
    result += on
    max_result = max(max_result, result)

print(max_result)