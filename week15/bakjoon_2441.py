# 2441번 브론즈3 별찍기4

n=int(input())

for i in range(n, 0, -1):
    print(" "*(n-i) + "*"*i)