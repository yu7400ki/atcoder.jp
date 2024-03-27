N = int(input())
a, b = sorted(map(int, input().split()))
c, d = sorted(map(int, input().split()))


if a < c < b < d or c < a < d < b:
    print(4)
else:
    print(3)
