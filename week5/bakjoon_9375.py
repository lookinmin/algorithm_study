#패션왕 신해빈, 실버3

t = int(input())

for i in range(t):
    n = int(input())
    clothes = {}
    for j in range(n):
        style = list(input().split())           #style[0]은 옷 이름, style[1]은 종류
        if style[1] in clothes:                 #종류 겹치면
            clothes[style[1]].append(style[0])  #해당 옷 종류에 옷 이름 append
        else:
            clothes[style[1]] = [style[0]]      #종류 안겹치면 대입
    cnt = 1
    for k in clothes:
        cnt *= (len(clothes[k]) + 1)
    print(cnt - 1)                              #전부 다 안입을 경우의 수 제거

