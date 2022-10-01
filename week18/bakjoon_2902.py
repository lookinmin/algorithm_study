#구현, 브론즈2, KMP

name = input()
arr = name.split("-")
res = ""
for i in arr:
    res += i[0]

print(res)