#브루트포스-영화감독 숌 / 실버5

n = int(input())
apo = 666               #숫자는 666부터 시작
num = 0                 #몇번째 인지 알려줄 변수
while 1:                #무한루프 돌면서
    if '666' in str(apo):   #증가하는 수에 666이 있다면
        num += 1            #순서 증가
    if num == n:            #증가하다가 n까지 증가했다면
        print(apo)          #해당 수를 출력하고
        break               #종료
    apo += 1


