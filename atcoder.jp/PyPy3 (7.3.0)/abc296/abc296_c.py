N, X = map(int, input().split())
A = list(map(int, input().split()))

A_set = set(A)

for a in A:
    b = X + a
    if b in A_set:
        print("Yes")
        exit()

print("No")
