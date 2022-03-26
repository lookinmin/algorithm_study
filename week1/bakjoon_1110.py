n = int(input())

num = n
cnt = 0
while True :
    n1 = num // 10
    n2 = num % 10
    a = (n1 + n2) % 10
    num = (n2 * 10) + a
    cnt = cnt + 1
    if num == n:
        break

print(cnt)