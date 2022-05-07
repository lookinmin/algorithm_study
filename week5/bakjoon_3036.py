#링, 실버3
n = int(input())
data = list(map(int, input().split()))

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

for i in range(1, n):
    num = gcd(data[0], data[i])
    print("{}/{}".format(data[0]//num, data[i]//num))

