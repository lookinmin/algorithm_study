#백준 정렬 4번, 실버3
import sys
import numpy
from collections import Counter

n = int(sys.stdin.readline())


arr=[]
for i in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()
print(round(numpy.mean(arr)))    #합 / 갯수 = 산술평균
print(round(numpy.median(arr)))        #중앙값

cnt_li = Counter(arr).most_common()
if len(cnt_li) > 1 and cnt_li[0][1]==cnt_li[1][1]: #최빈값 2개 이상
    print(cnt_li[1][0])
else:
    print(cnt_li[0][0])

c = len(arr)-1                  #제일 마지막 원소
print(arr[c] - arr[0])          #범위