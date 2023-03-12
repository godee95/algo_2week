import sys

N = int(sys.stdin.readline().rstrip())
arr1 = list(map(int, sys.stdin.readline().rstrip().split()))

M = int(sys.stdin.readline().rstrip())
arr2 = list(map(int, sys.stdin.readline().rstrip().split()))

# 탐색 전에 arr1을 정렬해야함.
arr1.sort()

def binary_search(arr1, target):
    pl = 0 # 젤 처음 index
    pr = len(arr1) - 1 # 젤 마지막 index

    while pl <= pr:
        idx = (pl + pr) // 2 # 중간 index
        if arr1[idx] == target:
            return 1
        elif arr1[idx] < target:
            pl = idx + 1
        elif arr1[idx] > target:
            pr = idx - 1

    return 0 

# 이진 탐색은 O(NlogN)
for target in arr2:
    print(binary_search(arr1, target))

# 숏 코딩 
# O(N)
# for target in arr2:
#     print('1' if target in arr1 else '0')

