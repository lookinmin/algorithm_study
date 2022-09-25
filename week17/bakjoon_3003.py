#구현, 브론즈5, 킹,퀸,룩,비숍,나이트, 폰

from sys import stdin
find = list(map(int, stdin.readline().split()))

set = [1, 1, 2, 2, 2, 8]
result = []

for i in range(len(set)):
    result.append(set[i] - find[i])

print(*result)