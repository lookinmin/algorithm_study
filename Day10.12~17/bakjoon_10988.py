# 구현, 브론즈2, 펠린드롬인지 확인하기

word = input()

if word[::-1] == word:
    print(1)
else:
    print(0)