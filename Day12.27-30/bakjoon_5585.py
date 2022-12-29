# Greedy, 브론즈2, 거스름돈

n = int(input())

res = 1000 - n
cnt = 0
while True:
    if res - 500 >= 0:
        cnt += 1
        res -= 500
    elif res - 100 >= 0:
        cnt += 1
        res -= 100
    elif res - 50 >= 0:
        cnt += 1
        res -= 50
    elif res - 10 >= 0:
        cnt += 1
        res -= 10
    elif res - 5 >= 0:
        cnt += 1
        res -= 5
    elif res - 1 >= 0:
        cnt += 1
        res -= 1

    if res == 0:
        break

print(cnt)