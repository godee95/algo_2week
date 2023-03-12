import sys

N = int(sys.stdin.readline().rstrip())

# 1 2 3 1 2 1

stack = []
for _ in range(N):
    stack.append(int(sys.stdin.readline().rstrip()))

flag = stack.pop()

cnt = 1
while stack:
    top = stack[-1]
    if top > flag:
        flag = stack.pop() # 기준이 바뀜! 3으로 바뀐 경우.
        cnt += 1
    else:
        stack.pop()

print(cnt)
