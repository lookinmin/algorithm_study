#백트래킹 4번, 실버3

n ,m = map(int, input().split())

answer = []

def dfs(depth):
    if len(answer) == m:
        print(" ".join(map(str, answer)))
        return
    for i in range(depth, n+1):
        answer.append(i)
        dfs(i)
        answer.pop()

dfs(1)