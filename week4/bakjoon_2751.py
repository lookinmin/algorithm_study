#정렬 2번, 수 오름차순 정렬

n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)

arr.sort()

for i in range(n):
    print(arr[i])