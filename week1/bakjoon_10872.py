#팩토리얼 브론즈 3

n = int(input())    #n! 할 정수 입력

result = 1          #곱해야하므로 결과값을 1에서 시작

if n == 0:          #입력값이 0 이면 1 출력
    print(result)
else :              #입력값이 0이 아니면
    for i in range(n):  #n까지 반복하면서
        result *= (n-i) #result * n -> result * n-1 ...
    print(result)

    #-------------재귀사용--------------------

def factorial(n):
    result = 1
    if n > 0:
        result = n*factorial(n-1)
    return result
print(factorial(n))





