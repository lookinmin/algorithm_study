# 그리디 알고리즘 실버1 회의실 배정
# 2-2에 배운 회의실 배정 코드화

n = int(input())
arr = []
cnt, last = 0, 0
for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])

# 시작시간 기준 정렬
arr.sort()
# 끝나는 시간 기준 한번 더
arr.sort(key=lambda t: t[1])

for i, j in arr:
    if i >= last:
        cnt +=1
        last = j

print(cnt)