import sys

N, K = map(int, input().split())
X = []
for _ in range(N):
    X.append(int(sys.stdin.readline()))

pl = min(X)
pr = pl + K
ans = 0

while pl <= pr:
    pc = (pl + pr) // 2
    hap = 0
    for i in X:
        if pc >= i:
            hap += pc - i

    if hap == K:
        ans = pc
        break
    elif hap > K:
        pr = pc - 1
    else:
        pl = pc + 1
        ans = pc

print(ans)