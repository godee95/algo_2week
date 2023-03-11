from sys import stdin
input = lambda: stdin.readline()

N, C = map(int, input().split())
homes = []
for i in range(N):
    homes.append(int(input()))

homes.sort()

pl, pr = 1, homes[N-1] - homes[0]   # 집 사이의 최소, 최대 거리

while pl <= pr:
    pc = (pl + pr) // 2
    prev = homes[0]
    put = 1

    for i in range(1, N):
        if homes[i] - prev >= pc:
            put += 1
            prev = homes[i]

    if put >= C:
        pl = pc + 1
    else:
        pr = pc - 1

print(pr)