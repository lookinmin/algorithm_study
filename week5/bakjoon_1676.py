#팩토리얼 0의 갯수, 실버4

from math import factorial

n = int(input())

result = list(str(factorial(n)))

num = len(result) - 1
cnt = 0
for i in range(num, 0, -1):
    if result[i] == "0":
        cnt += 1
    else:
        break

print(cnt)