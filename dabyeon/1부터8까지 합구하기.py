# Recusive로 접근

# 1~8 까지 합을 1~4(1~2/3~4) / 5~8(5~6/7~8) 까지 합으로 나누기
# 1~2(1/2), 3~4(3/4), ...
# base case = 1,2,3,4, ...

def recusive_sum(start, end):
    if start == end:
        return start
    mid = (start + end) // 2
    return recusive_sum(start, mid) + recusive_sum(mid+1, end)

print(recusive_sum(1, 100)) 