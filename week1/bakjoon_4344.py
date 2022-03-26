#브론즈 1

c = int(input())

for i in range(c):
    test_li = list(map(int, input().split())) #list의 인자를 int형으로 split해서 받는다
    avg = sum(test_li[1:])/test_li[0]         #놓친부분 : 파이썬은 [1:]을 통해 index = 1 부터 끝까지 접근 가능 : slicing
    cnt = 0
    for i in test_li[1:] :                      # i 가 1부터 list의 끝까지
        if i > avg :                            # index가 avg보다 크다면
            cnt += 1                            # 개수 증가
    rate = cnt / test_li[0] * 100               # 개수만큼을 비율화
    print(f'{rate:.3f}%')