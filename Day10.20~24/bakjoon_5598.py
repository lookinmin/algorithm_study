# 문자열, 브론즈2, 카이사르 암호

s = list(input())
arr = []
for i in s:
    k = ord(i) - 3
    if k < ord('A'):
        k += 26
    arr.append(chr(k))

print("".join(arr))