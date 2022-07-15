#입력과 출력, 브론즈3, 열 개씩 끊어 출력하기

s = input()
cnt = 0
for i in s:
    cnt += 1
    print(i, end="")
    if cnt%10 == 0:
        print("\n", end="")