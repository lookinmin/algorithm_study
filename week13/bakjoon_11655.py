# 문자열, 브론즈1, ROT13
# 알파벳 13글자씩 밀기

s = input()

for i in s:
    if i.islower():
        print(chr(97+(ord(i)+13-97)%26), end="")
    elif i.isupper():
        print(chr(65+(ord(i)+13-65)%26), end="")
    else:
        print(i, end="")