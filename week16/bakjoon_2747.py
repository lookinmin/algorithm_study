# 피보나치 수 브론즈2

n = int(input())


def Fibo(n):
    curr, next = 0, 1
    for i in range(n):
        curr, next = next, curr + next
    return curr

print(Fibo(n))