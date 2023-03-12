# ( 무조건 push
# )면 비어있는지 확인 비어있으면 바로 NO출력
# )고 비어있지 않으면 pop

import sys

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    stack = []
    flag = True
    str = sys.stdin.readline().rstrip()

    for e in str:
        if e == '(':
            stack.append(e)
        else:
            if len(stack) == 0:
                flag = False
                break
            else:
                stack.pop()
    if len(stack) != 0:
        flag = False
    print("NO") if flag == False else print('YES')