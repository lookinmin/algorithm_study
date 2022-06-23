#백트래킹 1번, 실버3 -> itertools pernutation 활용

from itertools import permutations

#삼성 코테에서는 itertools 사용 불가, DFS 위주의 문제 풀이 권장됨

n, m = map(int, input().split())
nums = [num + 1 for num in range(n)]
for i in permutations(nums, m):
    for j in i:
        print(j, end=" ")
    print()

