

from sys import stdin
arr = list(map(int, stdin.readline().split()))      # 입력


def quick_sort(arr):                                # 퀵정렬 함수 선언 매개변수 = 입력받은 배열
    if len(arr) <= 1:                               # 배열의 원소가 하나 밖에 없다면,
        return arr                                  # 종료
    pivot = arr[len(arr)-1]                         # pivot = 배열의 마지막 원소
    lesser_arr, equal_arr, greater_arr = [], [], [] # pivot보다 작은 원소들이 들어갈 배열, pivot과 같은 값들, pivot보다 큰 값들이 들어갈 배열을 선언
    for num in arr:                                 # 입력 받은 배열 내의 원소들을 처음부터 끝까지 탐색하면서
        if num < pivot:                             # 현재 탐색 중인 원소가 pivot보다 작은 경우,
            lesser_arr.append(num)                  # 작은 값들이 들어갈 배열에 추가
        elif num > pivot:                           # 현재 탐색 중인 원소가 pivot보다 큰 경우,
            greater_arr.append(num)                 # 큰 값들이 들어갈 배열에 추가
        else:                                       # pivot과 탐색중인 원소의 값이 같다면,
            equal_arr.append(num)                   # 같은 값들 배열에 추가
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)     # 작은 값들과, 큰 값들이 모여있는 양쪽 배열에 대해 재귀적으로 정렬 수행, 같은 값들끼리 있는 배열은 정렬 필요 없음
                                                                            # 정렬 후, 배열의 합 연산으로 3개의 배열을 하나로 합쳐 return


resultArr = quick_sort(arr)                         # 정렬된 결과를 받아줄 배열 변수 선언 = 정렬된 배열

print(*resultArr, end=" ")                          # 정렬된 배열내의 원소를 띄어쓰기 하여 출력