# 2920번 브론즈2 음계

arr = list(map(int, input().split()))

if arr == sorted(arr):
    print("ascending")
elif arr == sorted(arr, reverse=True):
    print("descending")
else:
    print("mixed")