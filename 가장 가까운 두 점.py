import sys
input = sys.stdin.readline

n = int(input())
points = []

for _ in range(n):
    points.append(list(map(int, input().split())))
points.sort()

def getDist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def dac(pl, pr):
    if pl == pr:
        return float('inf')

    pc = (pl + pr) // 2
    minDist = min(dac(pl, pc), dac(pc+1, pr))
    targetList = []

    for i in range(pc+1, pr+1):
        if (points[pc][0] - points[i][0]) ** 2 < minDist:
            targetList.append(points[i])
        else:
            break

    for i in range(pc, pl-1, -1):
        if (points[pc][0] - points[i][0]) ** 2 < minDist:
            targetList.append(points[i])
        else:
            break

    targetList.sort(key=lambda x: x[1])

    for i in range(len(targetList)-1):
        for j in range(i+1, len(targetList)):
            if (targetList[j][1] - targetList[i][1]) ** 2 < minDist:
                minDist = min(minDist, getDist(targetList[i], targetList[j]))
            else:
                break
    return minDist

print(dac(0, n-1))
