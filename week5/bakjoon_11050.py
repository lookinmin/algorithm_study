#이항계수1, 브론즈1

n, k = map(int,input().split())

a = 1
for i in range(k):
    a *= n
    n -= 1

b = 1
for i in range(k):
    b *= k
    k -= 1

print(int(a/b))
