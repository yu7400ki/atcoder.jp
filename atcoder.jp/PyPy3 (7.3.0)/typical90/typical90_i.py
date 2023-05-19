from math import acos, degrees
from itertools import permutations


class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def norm(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Vec({self.x}, {self.y})"


N = int(input())
XY = [Vec(*map(int, input().split())) for _ in range(N)]

ans = 0
for i, j, k in permutations(range(N), 3):
    p_i = XY[i]
    p_j = XY[j]
    p_k = XY[k]
    u = p_j - p_i
    v = p_k - p_i
    cos = u.dot(v) / (u.norm() * v.norm())
    deg = degrees(acos(cos))
    ans = max(ans, deg)

print(ans)
