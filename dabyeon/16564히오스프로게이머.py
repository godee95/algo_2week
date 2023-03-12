# 캐릭터 N개
# 레벨 올릴 수 있는 최대치 K
# 가능한 최대 팀 목표 레벨 T를 출력

import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
X = [int(sys.stdin.readline().rstrip()) for _ in range(N)]


def binary(X, K):

    X.sort()

    max_point = float('-inf')
    # 기본적인 이분탐색에서 요구하는 값은 항상 mid값중 최대이거나, 최소인 값들이라는 점이다. 
    pl = min(X)
    pr = pl + K

    while pl <= pr:
        mid = (pl + pr) // 2 # 팀 목표 레벨
        
        temp = 0
        for x in X:
            if x < mid:
                temp += mid - x
            # if temp > K:
            #     break
        
        if temp <= K:
            max_point = max(max_point, mid)
            pl = mid + 1
        else:
            pr = mid -1
    return max_point

print(binary(X, K))

