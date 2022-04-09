#나이순 오름차순 정렬, 입력순 정렬, 실버5

n = int(input())
arr = []
cnt = 0
for i in range(n):
    a, n = input().split()
    a = int(a)
    arr.append([a, cnt, n])             #입력받은 순서 제어해주기 위해 cnt를 같이 append
    cnt += 1                            #append 이후에 cnt ++

arr.sort()                              #정렬

for i in arr:
    print(i[0], i[2])


