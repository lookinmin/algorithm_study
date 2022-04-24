#좌표 정렬하기 2, 실버5

n = int(input())

arr=[]                                      #입력받을 배열
for i in range(n):
    x, y = map(int, input().split())        #좌표 2차원 리스트로 입력
    arr.append([y, x])                      #y기준 정렬이므로 y,x 순으로 append

arr.sort()                                  #배열 정렬

for y, x in arr:                            #x, y 순으로 출력
    print(x, y)

