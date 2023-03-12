# Recusive 접근

# 10^11 승은 10^5/10^6으로 나눌 수 있음

# 해당 코드 함수 범위를 반으로 나눠서 재귀적으로 호출.
# 함수 호출 횟수가 증가
# 이러한 호출 횟수 증가로 인한 시간복잡도 해결은 분할 정복 기반 알고리즘 이용!


import sys

A, B, C = map(int, sys.stdin.readline().rstrip().split())

# A = 10
# B = 11
# C = 12

def recusive_mul(start, end):
    if start == end:
        return A

    mid = (start + end) // 2
    return recusive_mul(start, mid) * recusive_mul(mid+1, end)

print(recusive_mul(1, B) % C)

# -----------------------------------------------------------------

result = 1
while B > 0:
    if B % 2 == 1: # 홀수 일 경우
        result = (result * A) % C
    A = (A * A) % C
    B //= 2

print(result)

# print(2^5)