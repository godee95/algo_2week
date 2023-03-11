N = int(input())
fluids = list(map(int, input().split()))
fluids.sort()

if fluids[0] >= 0:
    print(fluids[0], fluids[1])
elif fluids[-1] <= 0:
    print(fluids[-2], fluids[-1])
else:
    pl, pr = 0, N-1
    result = abs(fluids[pl] + fluids[pr])
    ans = [fluids[pl], fluids[pr]]
    while pl < pr:
        sum = fluids[pl] + fluids[pr]

        if abs(sum) < result:
            result = abs(sum)
            ans = [fluids[pl], fluids[pr]]
            if result == 0:
                break
        if sum < 0:
            pl += 1
        else:
            pr -= 1

    print(ans[0], ans[1])