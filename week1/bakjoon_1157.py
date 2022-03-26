#가장 많이 사용된 알파벳 찾기, 브론즈1

str = input().upper()
arr = []

unique = list(set(str))

for i in unique :
    cnt = str.count(i)
    arr.append(cnt)

if arr.count(max(arr)) > 1:
    print('?')
else :
    max = arr.index(max(arr))
    print(unique[max])

