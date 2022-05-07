# 최소공배수, 실버5, 유클리드 알고리즘

t = int(input())

small = []
big = []
for i in range(t):
    a, b = map(int, input().split())
    small.append(a)
    big.append(b)

result = []


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b / gcd(a, b)


for i in range(t):
    result.append(int(lcm(small[i], big[i])))

for i in result:
    print(i)
