# 피보나치, 브론즈2

num = int(input())          #입력 받을 수


def Get_pibo(n):            #재귀함수
    result = 0
    if n == 0:              #0이나 1이면 0, 1 리턴
        return 0
    elif n == 1:
        return 1
    else:
        result = Get_pibo(n - 1) + Get_pibo(n - 2)  #n이 3부터, 이전함수의 결과값을 더함
    return result


print(Get_pibo(num))
