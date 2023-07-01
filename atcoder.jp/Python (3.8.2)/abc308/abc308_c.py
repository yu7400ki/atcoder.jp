from fractions import Fraction

N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]

AB = sorted(enumerate(AB), key=lambda x: Fraction(x[1][0], x[1][0] + x[1][1]), reverse=True)
AB = map(lambda x: x[0] + 1, AB)

print(*AB, sep=" ")
