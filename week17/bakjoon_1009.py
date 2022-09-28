#구현, 브론즈2, 분산처리

# from sys import stdin
# t = int(stdin.readline())
# res = 0
# for i in range(t):
#     a, b = map(int, stdin.readline().split())
#     while True:
#         res = a**b % 10
#         res // 10
#         if res < 10:
#             break
#     if res == 0:
#         print(10)
#     else:
#         print(res)
# 시간초과 남


T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    a = a % 10

    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 4 or a == 9:
        b = b % 2
        if b == 1:
            print(a)
        else:
            print((a * a) % 10)
    else:
        b = b % 4
        if b == 0:
            print((a ** 4) % 10 % 10 % 10)
        else:
            print((a ** b) % 10 % 10 % 10)