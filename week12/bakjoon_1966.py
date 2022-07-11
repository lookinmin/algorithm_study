# 큐와덱, 실버3, 프린터 큐

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    num = list(map(int, input().split()))
    idx = [0 for i in range(n)]
    idx[m] = 1
    cnt = 0
    while 1:
        if num[0] == max(num):
            cnt += 1
            if idx[0] == 1:
                print(cnt)
                break
            else:
                num.pop(0)
                idx.pop(0)
        else:
            num.append(num[0])
            num.pop(0)
            idx.append(idx[0])
            idx.pop(0)

