N = int(input())
P = list(map(int, input().split()))
Q = int(input())

for _ in range(Q):
    a, b = map(int, input().split())
    if P.index(a) < P.index(b):
        print(a)
    else:
        print(b)
