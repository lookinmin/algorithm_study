#백준 정렬 8번, 실버5
import sys
n = int(sys.stdin.readline())

arr = []
for i in range(n):
    arr.append(sys.stdin.readline().strip())

final = set(arr)        #중복 제거
arr = list(final)       #중복이 제거된 배열을 다시 list화
arr.sort()              #단어 순으로 정렬
arr.sort(key=len)       #길이 순으로 재정렬

for i in arr:
    print(i)
