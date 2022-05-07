# 백준 정렬10, 실버3
# 리스트안에서 인덱스의 크기 순서 출력
import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
change = list(sorted(set(arr)))  #set() -> 집합화, 중복 자동 제거

dic = {change[i]: i for i in range(len(change))}

for i in arr:
    print(dic[i], end=" ")
