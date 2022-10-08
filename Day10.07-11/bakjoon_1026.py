# 정렬, 실버4, 보물

N = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
res = []
s_arr1 = sorted(arr1, reverse=True)
s_arr2 = sorted(arr2)

for i in range(len(s_arr1)):
    res.append(s_arr1[i] * s_arr2[i])

print(sum(res))
