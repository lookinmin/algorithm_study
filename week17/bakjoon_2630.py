#분할정복, 실버2, 색종이 만들기

from sys import stdin
n = int(stdin.readline())
paper = [list(map(int, stdin.readline().split())) for _ in range(n)]
result = []

def DAC(x, y, n):
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                DAC(x, y, n//2)
                DAC(x, y+n//2, n//2)
                DAC(x+n//2, y, n//2)
                DAC(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)

DAC(0,0,n)
print(result.count(0))
print(result.count(1))