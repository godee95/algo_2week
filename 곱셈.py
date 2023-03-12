A, B, C = map(int, input().split())

def DaC(A, B):
    if B == 1:
        return A % C

    temp = DaC(A, B//2)

    if B % 2 == 0:
        return temp * temp % C
    else:
        return temp * temp * A % C

print(DaC(A, B))