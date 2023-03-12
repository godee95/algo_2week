import sys

str = sys.stdin.readline().rstrip()
# str = '('

stack = []
flag = True
for e in str:
    if e == '(' or e == '[':
        stack.append(e)
    elif e == ')':
        result = 0
        while True:
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop() # ( 스택에서 빼줌
                result = 2 if result == 0 else result * 2
                stack.append(result)
                break
            elif len(stack) == 0 or stack[-1] == '[':
                flag = False
                break
            result += stack.pop()
    elif e == ']':
        result = 0
        while True:
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop() # ( 스택에서 빼줌
                result = 3 if result == 0 else result * 3
                stack.append(result)
                break
            elif len(stack) == 0 or stack[-1] == '(': # or 은 앞 조건을 먼저 보고 True면 뒷조건 안보고 바로 참으로 실행!
                flag = False
                break
            result += stack.pop()

s = 0
while(len(stack) > 0):
    if type(stack[-1]) != int:
        flag = False
        break
    s += stack.pop()

if flag == False:
    print(0)
else:
    print(s)
