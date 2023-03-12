import sys

N = int(sys.stdin.readline().rstrip())

stack = []
for _ in range(N):
    n = int(sys.stdin.readline().rstrip())
    stack.append(n) if n != 0 else stack.pop()

print(sum(stack))