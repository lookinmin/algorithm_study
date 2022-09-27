#구현, 브론즈1, 팰린드롬수
# 우영우 숫자 찾기

while True:
    n = input()
    if n == "0":
        break

    if n == n[::-1]:
        print("yes")
    else:
        print("no")