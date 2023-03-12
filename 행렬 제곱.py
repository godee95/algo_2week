import sys
input = sys.stdin.readline

N, B = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

def dot(A, B):
    C = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] += A[i][k] * B[k][j]
                C[i][j] %= 1000

    return C

def DaC(A, B):
    if B == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] %= 1000
        return A

    temp = DaC(A, B//2)

    if B % 2 == 0:
        return dot(temp, temp)
    else:
        return dot(dot(temp, temp), A)

for r in DaC(A, B):
    print(*r)