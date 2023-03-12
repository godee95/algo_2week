# 잡을 수 있는 동물의 수는 사정 거리 내에 있는지 확인 후 cnt
# 사정 거리가 최소 최대.

import sys

m, n, l = map(int, sys.stdin.readline().rstrip().split())
M = list(map(int, sys.stdin.readline().rstrip().split()))
animal = list(map(int, sys.stdin.readline().rstrip().split()) for _ in range(n))

# m, n, l = 4, 8, 4
# M = [6, 1, 4, 9]
# animal = [[7, 2], [3, 3], [4, 5], [5, 1], [2, 2], [1, 4], [8, 4], [9, 4]]

M.sort() # [1, 4, 6, 9]

cnt = 0

# 동물의 각 위치 
for a, b in animal:
    # 사격 범위 벗어나므로 넘어가기
    if b > l:
        continue

    pl = 0 # 가격 배열 index 첫번째 값
    pr = m - 1 # 사격 배열 index 마지막 값

    # 해당 동물이 사격 거리 내에 있는지 확인
    while pl <= pr:
        mid = (pl + pr) // 2

        # l <= |a-x| + b(일차함수)에 해당하는 동물이 각 사대에서 잡을 수 있는 동물이기에 위와 같은 식으로 바꿀 수 있다.
        if M[mid] < a + b - l: #4 lower y = x에서 y축 L만큼 올린거
            pl = mid + 1
        elif M[mid] > a - b + l: # upper y = -x에서 y축 L만큼 올린거
            pr = mid - 1
        else:
            cnt += 1
            break

print(cnt)

