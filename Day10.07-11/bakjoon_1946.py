# 정렬, 실버1, 신입 사원

# 서류심사, 면접시험 적어도 하나가 다른 지원자보다 떨어지지 않아야 선발

from sys import stdin
T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    arr = [0] * N
    for i in range(N):
        a, b = map(int, stdin.readline().split())
        arr[i] = [a, b]
    arr1 = sorted(arr)
    cnt = 1
    man = arr1[0][1]
    for i in range(1, N):
        if arr1[i][1] < man:
            man = arr1[i][1]
            cnt += 1

    print(cnt)


