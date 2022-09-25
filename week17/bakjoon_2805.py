#이분탐색, 실버2, 나무자르기

from sys import stdin
n, m = map(int, stdin.readline().split())
# n = 나무의 수, m = 가져갈 나무의 길이)
height = list(map(int, stdin.readline().split()))

# 접근법 : 벌목 높이를 움직여 필요 나무 길이를 채우는 지 확인

start = 1
end = max(height)

# 3) mid를 start와 end의 중간으로 두고, 모든 값에서 mid를 빼 총 어느정도 길이의 벌목된 나무가 나오나 살펴본다.
# 4-1) 벌목나무가 목표치 이상이면 mid+1을 start로 두고 다시 while문 반복
# 4-2) 벌목나무가 목표치 이하면 mid-1을 end로 두고 다시 while문 반복
# 5) start와 end가 같아지면: 조건을 만족하는 최대의 나무 절단 높이를 찾으면 탈출한다.
# 6) 결과값인 end출력

while start <= end:
    mid = (start+end)//2
    treeSum = 0
    for i in height:
        if i >= mid:
            treeSum += i - mid

    if treeSum >= m:
        start = mid+1
    else :
        end = mid -1

print(end)



