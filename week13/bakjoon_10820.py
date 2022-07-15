# 문자열 분석, 브론즈2, 소문자, 대문자, 숫자, 공백의 수
import sys

while 1:
    s = sys.stdin.readline().rstrip("\n")

    if not s:
        break

    cnt1, cnt2, cnt3, cnt4 = 0, 0, 0, 0
    for i in s:
        if i.islower():
            cnt1 += 1
        elif i.isupper():
            cnt2 += 1
        elif i.isdigit():
            cnt3 += 1
        elif i.isspace():
            cnt4 += 1
    print(cnt1, cnt2, cnt3, cnt4, end=" ")

