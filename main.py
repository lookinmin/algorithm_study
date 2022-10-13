

from sys import stdin
arr = list(map(int, stdin.readline().split()))      # 입력


def quick_sort(arr):                                # 퀵정렬 함수 선언 매개변수 = 입력받은 배열
    if len(arr) <= 1:                               # 배열의 원소가 하나 밖에 없다면,
        return arr                                  # 종료
    pivot = arr[len(arr)-1]                         # pivot = 배열의 마지막 원소
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)


resultArr = quick_sort(arr)

print(*resultArr, end=" ")