A, B = map(int, input().split())

ay, ax = divmod(A - 1, 3)
by, bx = divmod(B - 1, 3)

if abs(ax - bx) <= 1 and ay == by:
    print("Yes")
else:
    print("No")
