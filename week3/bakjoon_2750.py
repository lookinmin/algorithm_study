# 정렬 1번, 브론즈 1

# 삽입정렬

num = int(input())
array = []
for i in range(num):
    x = int(input())
    array.append(x)


def insert_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):  # i번째 부터 첫번째 원소까지 역순으로 비교
            if arr[j - 1] > arr[j]:  # 앞 원소가 뒤 원소보다 크면
                arr[j - 1], arr[j] = arr[j], arr[j - 1]  # 자리 바꿔줌


insert_sort(array)
for i in array:
    print(i)
