# 이분 탐색, 결정 문제
# 이분적일 때 사용할 수 있는 탐색 기법
# 많은 최적화 문제는 이분 탐색으로 풀 수 있습니다.

# 경계는 항상 [lo, hi]에서 존재
# while(lo+1 < hi)
# mid = (lo+hi) / 2
# check(lo) == check(mid)라면 lo= mid 
# check(hi) == check(mid)라면 hi=mid
# 검색이 끝난뒤 lo의 다음값은 hi이다. lo+1 = hi(탈출 조건)

# Parametric Search
# 만약 최적화 문제를 결정 문제로 구할 수 있음 만약, 답의 분포가 F~T인데 
# 정답이 가장 큰 F라면 lo를, 가장 작은 T라면 hi를 출력해주면 됩니다.

import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
trees = list(map(int, sys.stdin.readline().rstrip().split()))

target = M
result = 0

def cut_tree(trees, mid):
    return sum(tree - mid for tree in trees if tree > mid)

def binary_search(result, trees, target):
    pl = 0 # 가장 작은값은 0
    pr = max(trees)# 나무 중 가장 큰 값

    while pl <= pr:
        mid_idx = (pl + pr) // 2 # 중간 index
        if cut_tree(trees, mid_idx) >= target:
            pl = mid_idx+1
            result = mid_idx
        elif cut_tree(trees, mid_idx) < target:
            pr = mid_idx-1
    return result

    while pl + 1 < pr:
        mid_idx = (pl + pr) // 2 # 중간 index
        if cut_tree(trees, mid_idx) >= target:
            pl = mid_idx
        elif cut_tree(trees, mid_idx) < target:
            pr = mid_idx
    return pl

print(binary_search(result, trees, target))