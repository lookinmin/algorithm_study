# 구현, 브론즈2, 그릇


arr = list(str(input()))

res = 0
for i in range(len(arr)):
    if i == 0:
        res += 10
    elif arr[i] == arr[i-1]:
        res += 5
    else:
        res += 10

print(res)

