H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
T = [list(input()) for _ in range(H)]

def transpose(A):
    return list(map(list, zip(*A)))

S = transpose(S)
T = transpose(T)

S.sort()
T.sort()

if S == T:
    print("Yes")
else:
    print("No")
