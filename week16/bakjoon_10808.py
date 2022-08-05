# 알파벳 개수, 브론즈 4

s = input()
arr = [0]*26

for i in s:
    arr[ord(i)-97] += 1

print(*arr)