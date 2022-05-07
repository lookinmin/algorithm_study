#최대공약수와 최소공배수, 실버5

a, b = map(int, input().split())

for i in range(1, min(a, b)+1):
    if(a % i == 0) and (b % i == 0):
        maxGong = i

data1 = []
data2 = []
for i in range(1, b+1):
    data1.append(i*a)
for i in range(1, a+1):
    data2.append(i*b)

for i in data1:
    if i in data2:
        minGong = i
        break

print(maxGong)
print(minGong)


