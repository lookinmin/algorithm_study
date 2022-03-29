#브루트포스-덩치, 실버5

n = int(input())
a = []
for i in range(n):          #2중 리스트 선언 및 동적으로 값 할당
    a.append([])
    x, y = map(int, input().split())
    a[i].append(x)
    a[i].append(y)

for i in a:                 #일단 index의 rank를 1로 지정 후,
    rank = 1
    for j in a:             #연속하는 index들과 비교하면서 자신보다 덩치가 클 때마다 rank + 1
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = " ")
