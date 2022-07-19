# 힙정렬 알고리즘

import heapq

def heap_sort(nums):
    heap = []
    for i in nums:
        heapq.heappush(heap, i)

    sorted_arr = []
    while heap:
        sorted_arr.append(heapq.heappop(heap))
    return sorted_arr

print(heap_sort([4, 1, 7, 3, 8, 5]))