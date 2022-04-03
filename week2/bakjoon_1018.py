#브루트포스-체스판/실버5
n, m = map(int, input().split())
check = []

for i in range(n):
    check.append(input())

result = []

for a in range(n - 7):                              # 세로로 증가하면서 (세로로 1칸씩 내려감)
    for i in range(m - 7):                          # 가로로 증가하면서 (가로로 1칸씩 넘어감)
        idx1 = 0
        idx2 = 0
        for b in range(a, a + 8):                  # 8x8로 구역 나눔
            for j in range(i, i + 8):              # 8X8 범위를 B와 W로 번갈아가면서 검사
                if (j + b)%2 == 0:                 # 짝수일 때,
                    if check[b][j] != 'W':
                        idx1 += 1                   # 원래 있어야 될 색이랑 다르면 +1 -> w로 시작
                    if check[b][j] != 'B':
                        idx2 += 1                   # B로 시작
                else:                               # 홀수일 때,
                    if check[b][j] != 'B':
                        idx1 += 1
                    if check[b][j] != 'W':
                        idx2 += 1
        result.append(idx1)                          # W로 시작했을 때 칠해야 할 부분
        result.append(idx2)                          # B로 시작했을 때 칠해야 할 부분

print(min(result))