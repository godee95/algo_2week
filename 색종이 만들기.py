import sys

input = sys.stdin.readline
N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

result = []

def solution(x, y, N):
    color = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if paper[i][j] != color:
                solution(x, y, N//2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y, N//2)
                solution(x+N//2, y+N//2, N//2)
                return
    if color == 1:
        result.append(1)
    else:
        result.append(0)

solution(0, 0, N)
print(result.count(0))
print(result.count(1))