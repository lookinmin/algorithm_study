# 구현, 브론즈2, 대표값 2
arr = []
for _ in range(5):
    arr.append((int(input())))

arr.sort()
print(sum(arr)//5)
print(arr[2])
