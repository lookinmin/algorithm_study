#백트래킹 1번, DFS를 통한 풀이

n, m = map(int, input().split())
answer = []
check = [0]*m

def dfs(depth):
    global  answer
    if depth == m:
        answer.append([*check])
    else :
        for i in range(n):
            if i + 1 in check:
                continue
            check[depth] = i+1
            dfs(depth + 1)
            check[depth] = 0

dfs(0)

for i in answer:
    print(*i)
