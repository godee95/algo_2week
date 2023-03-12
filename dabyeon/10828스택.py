import sys

N = int(sys.stdin.readline().rstrip())

stack = []
for _ in range(N):
    str = sys.stdin.readline().rstrip().split()

    if str[0] == "push":
        stack.append(int(str[1]))
    elif str[0] == "pop":
        print(-1) if len(stack)==0 else print(stack.pop())
    elif str[0] == "size":
        print(len(stack))
    elif str[0] == "empty":
        print(1) if len(stack)==0 else print(0)
    elif str[0] == "top":
        print(-1) if len(stack)==0 else print(stack[-1])
