

from sys import stdin
arr = list(map(int, stdin.readline().split()))      # 입력


def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = end # 피벗은 첫 번째 원소
    left = start
    right = end-1
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start+1, right)
    quick_sort(array, right, end)


quick_sort(arr, 0, len(arr)-1)                         # 정렬된 결과를 받아줄 배열 변수 선언 = 정렬된 배열

print(*arr, end=" ")                          # 정렬된 배열내의 원소를 띄어쓰기 하여 출력