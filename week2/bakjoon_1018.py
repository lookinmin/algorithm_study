#브루트포스-체스판/실버5
n, m = map(int, input().split())
check = []

for i in range(n):
    check.append(input())

# 이후로 모르겠음

result = []

for a in range(n - 7):
    for i in range(m - 7):
        idx1 = 0
        idx2 = 0
        for b in range(a, a + 8):
            for j in range(i, i + 8):              # 8X8 범위를 B와 W로 번갈아가면서 검사
                if (j + b)%2 == 0:
                    if check[b][j] != 'W': idx1 += 1
                    if check[b][j] != 'B': idx2 += 1
                else :
                    if check[b][j] != 'B': idx1 += 1
                    if check[b][j] != 'W': idx2 += 1
        result.append(idx1)                          # W로 시작했을 때 칠해야 할 부분
        result.append(idx2)                          # B로 시작했을 때 칠해야 할 부분

print(min(result))