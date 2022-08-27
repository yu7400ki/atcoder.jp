class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
Cx, Cy = map(int, input().split())
Dx, Dy = map(int, input().split())

A = Point(Ax, Ay)
B = Point(Bx, By)
C = Point(Cx, Cy)
D = Point(Dx, Dy)

def in_tri(A, B, C, P):
    c1 = (B.x - A.x) * (P.y - A.y) - (B.y - A.y) * (P.x - A.x)
    c2 = (C.x - B.x) * (P.y - B.y) - (C.y - B.y) * (P.x - B.x)
    c3 = (A.x - C.x) * (P.y - C.y) - (A.y - C.y) * (P.x - C.x)
    return c1 >= 0 and c2 >= 0 and c3 >= 0 or c1 < 0 and c2 < 0 and c3 < 0

if in_tri(A, B, C, D) or in_tri(A, B, D, C) or in_tri(C, D, A, B) or in_tri(C, D, B, A):
    print("No")
else:
    print("Yes")