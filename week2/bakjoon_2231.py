# 브루트포스-분해합, 브론즈2

n = int(input())

for i in range(1, n+1):         #자연수 1부터 n까지 반복하면서
    num = sum((map(int, str(i))))   #i를 자릿수로 분해하여 더한값
    all = i + num               #i의 자릿수의 합 + i
    if all == n:                #all값이 n과 같다면, 생성자이므로
        print(i)                #출력
        break
    if i == n:                  #i가 n값까지 증가한다면
        print(0)                #생성자가 아님