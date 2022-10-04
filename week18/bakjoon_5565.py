# 구현, 브론즈3, 영수증

total = int(input())
arr = []
for i in range(9):
    arr.append(int(input()))

print(total - sum(arr))