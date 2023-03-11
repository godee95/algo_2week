import sys
input = sys.stdin.readline

M, N, L = map(int, input().split())
sh_area = list(map(int, input().split()))
sh_area.sort()
animals = []
for _ in range(N):
    x, y = map(int, input().split())
    animals.append((x, y))
cnt = 0
for animal in animals:
    x = animal[0]
    y = animal[1]
    if y <= L:
        pl, pr = 0, M-1
        while pl <= pr:
            pc = (pl + pr) // 2
            if abs(x - sh_area[pc]) <= L - y:
                cnt += 1
                break
            else:
                if x >= sh_area[pc]:
                    pl = pc + 1
                else:
                    pr = pc - 1

print(cnt)