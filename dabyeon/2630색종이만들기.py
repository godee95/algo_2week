# 1번째 는 N/4해서 모든 좌표가 0이거나 1인 사분면이 있으면 cnt올라감
# 2번째는 N/2해서 모든 좌표가 0이거나 1인 사분면이 있으면 cnt 올라감.
# 이런식으로 반복.

# divide and Conquer
# 기존 문제를 작은 부분 문제들로 나눔
# 각 부분 문제를 해결
# 부분 문제 솔루션을 통해 기존 문제 해결

# 작은 부분 문제들의 답을 도출!
# 무조건 나누면 안되고 그 문제 Base case인지 Recusive case인지 나눠야 함.

# 재귀적으로 진행되는 부분이 많음!

# 백준 2630번 색종이 만들기
# # Bace Case
# color = paper[x][y] # 기준 컬러
# # size 내에서 color(기준 컬러)와 다른 color있는지 
# for i in range(size):
#     for j in range(size):
#         if paper[i][j] != color:
#             print('쪼개야 해!')
#         else:
#             if color == 1:
#                 blue += 1
#             else:
#                 white += 1

import sys

size = int(sys.stdin.readline().rstrip())
paper = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(size)]

# paper = [[1, 1, 0, 0, 0, 0, 1, 1], 
#          [1, 1, 0, 0, 0, 0, 1, 1], 
#          [0, 0, 0, 0, 1, 1, 0, 0], 
#          [0, 0, 0, 0, 1, 1, 0, 0],
#          [1, 0, 0, 0, 1, 1, 1, 1],
#          [0, 1, 0, 0, 1, 1, 1, 1],
#          [0, 0, 1, 1, 1, 1, 1, 1],
#          [0, 0, 1, 1, 1, 1, 1, 1]]

# size = len(paper)


blue = 0
white = 0

def divide(x, y, size):
    global blue, white
    # Bace Case
    color = paper[x][y] # 기준 컬러
    # size 내에서 color(기준 컬러)와 다른 color있는지 
    for i in range(x, x+size):
        for j in range(y, y+size):
            if paper[i][j] != color:
                divide(x,y,size//2)
                divide(x,y+size//2,size//2)
                divide(x+size//2,y,size//2)
                divide(x+size//2,y+size//2,size//2)
                return # 분할 영역의 색이 다른 경우 함수 호출 중단.
    if color == 1:
        blue += 1
    else:
        white += 1
    return blue, white

divide(0,0,size)

# print(f'blue : {blue}, white: {white}')

print(white)
print(blue)
