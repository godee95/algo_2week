# 공유기가 각 이분법 범위에 설치하는 게 가장 이상적
# 가장 인접한 두 공유기 사이 거리를 최대(pl)로 만드는 문제
# 구하고자 하는게 두 집 사이의 거리(gap)
# 공유기가 각 이분법 범위에 설치하는 게 가장 이상적
# 가장 인접한 두 공유기 사이 거리를 최대(pl)로 만드는 문제
# 구하고자 하는게 두 집 사이의 거리(gap)
import sys

N, C = map(int, sys.stdin.readline().rstrip().split())
x = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

x.sort()

result = 0

def binary_search(result, x, C):
    pl = 1 # 가장 짧은 gap
    pr = x[-1] - x[0] # 가장 큰 gap

    while pl <= pr:
        mid = (pl + pr) // 2 # 중간 gap
        cur = x[0] # 가장 왼쪽 집은 반드시 공유기를 설치해야 한다.
        cnt = 1

        for i in range(1, len(x)):
            # 갈 수 있는 폭(mid)이 집사이의 폭(gap)보다 작으면 설치 가능
            if x[i] - cur >= mid:
                cur = x[i]
                cnt += 1

        if cnt >= C:
            pl = mid+1 # 공유기 다 설치할 수 있다면 mid 범위 늘리기
            result = mid
        else:
            pr = mid-1 # 공유기 다 설치할 수 없으면 mid 범위 줄이기
    return result
            
print(binary_search(0, x, C)) 

# mid중에서 가장 큰 mid을 찾는거지, while로 끝나고 나서 어느 위치로 수렴한 mid이 아니라,
# 중간중간 mid이 작아졌다 커졌다 반복.
# 그 때 조건을 만족하면서 가장 컸던 mid이 문제가 원하는 답임!