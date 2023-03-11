N, M = map(int, input().split())
trees = list(map(int, input().split()))
pl, pr = 1, max(trees)


while pl <= pr:
    pc = (pl + pr) // 2
    cut = 0

    cut = sum(tree - pc if tree > pc else 0 for tree in trees)

    if cut < M:
        pr = pc - 1
    else:
        pl = pc + 1

print(pr)