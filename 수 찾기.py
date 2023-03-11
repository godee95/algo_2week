N = int(input())
A = list(map(int, input().split()))
M = int(input())
keys = list(map(int, input().split()))
A.sort()

for num in keys:
    pl, pr = 0, N - 1
    isContain = False

    while pl <= pr:
        pc = (pl + pr) // 2
        if num == A[pc]:
            isContain = True
            print(1)
            break
        elif num < A[pc]:
            pr = pc - 1
        else:
            pl = pc + 1

    if not isContain:
        print(0)
