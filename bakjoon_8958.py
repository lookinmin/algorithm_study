num = int(input())      #몇 개 입력할건지

for i in range(num):
    ox_list = list(input())     #반복하면서 list type으로 입력받고
    score = 0                   #점수는 1,2,3 이런식으로 증가하도록
    sum = 0                     #최종점수
    for ox in ox_list:
        if ox == 'O':
            score += 1          # 다음 인덱스가 O가 나올때마다 +1점씩
            sum += score
        else :
            score = 0
    print(sum)                  #최종결과를 출력