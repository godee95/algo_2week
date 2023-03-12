# 산성용액은 특정값 1~1,000,000,000 양의 정수
# 알칼리성 용액은 특정값 1부터 -1,000,000,000까지의 음의 정수

# 여러 용액 중 두 용액의 합이 0에 가까운 용액 만들기
# 두 용액을 혼합하여 특정값이 0에 가까운 용액을 만들려고 한다.

# 구간합 (Range Sum) 유투브로 찾아보기!!

# 0에 가깝다는 의미는 두 값의 차이가 가장 적다는 의미 -> min_diff를 찾기
# i-j 구간합 계산은 O(NlogN) 시간에 수행 가능
import sys

N = int(sys.stdin.readline().rstrip())

solutions = list(map(int, sys.stdin.readline().rstrip().split()))

target = 0
result = [0]*2
s = sorted(solutions)

def binary_search(s, target, result):
    min_diff = float("inf")

    for idx in range(len(s)-1):
        # idx 이전의 용액과의 합을 구하지 않고, idx와 같은 용액과의 합을 구하지 않게 됨!
        # 조합 개념 생각 idx와 mid_idx 값을 계속 비교하게됨.
        pl = idx+1 # 가장 작은 인덱스+1 
        pr = len(s) -1 # 가장 큰 인덱스

        while pl <= pr:
            mid_idx = (pl + pr) // 2

            if s[idx] + s[mid_idx] == target:
                result[0] = s[idx]
                result[1] = s[mid_idx]
                return result
            
            diff = abs(target - (s[idx] + s[mid_idx])) 
            if diff < min_diff:
                min_diff = diff
                result[0] = s[idx] # 이 값은 수시로 바뀜
                result[1] = s[mid_idx] # 이 값은 수시로 바뀜

            if s[idx] + s[mid_idx] >= target:
                pr = mid_idx - 1 # 합을 줄여주기
            else:
                pl = mid_idx + 1 # 합을 늘려주기

    return result


print(*binary_search(s, target, result))

# ==================== 다른 사람 코드 =======================

# 주어진 정수 배열 arr에서 두 수를 뽑아 합이 0에 가장 가까운 두 수를 찾아 내는 calcul 함수
# left 첫번째 인덱스
# right 마지막 인덱스 
# temp = arr[left] + arr[right]
# temp가 0에 가장 가깝다면, minLeft와 minRight를 갱신.
# temp가 0보다 크다면 right 이동시켜 합을 줄여주기
# temp가 0보다 작다면 left 이동시켜 합을 늘려주기

def calcul(n, arr):
    left = 0
    right = n-1
    arr.sort()
    diff = 2000000001
    minLeft = 0
    minRight = 0
    while left < right:
        temp = arr[left]+arr[right]
        if abs(temp) < diff:
            diff = abs(temp)
            minLeft = arr[left]
            minRight = arr[right]
        if temp > 0:
            right -= 1
            continue
        left += 1
    return minLeft, minRight

n = int(input())
l = list(map(int, input().split()))
result = calcul(n,l)
print(result[0], result[1])