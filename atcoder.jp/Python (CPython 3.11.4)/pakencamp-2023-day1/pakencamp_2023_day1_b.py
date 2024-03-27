N = int(input())
a, b = sorted(map(int, input().split()))
c, d = sorted(map(int, input().split()))

if (a, b) == (c, d):
    print(2)
elif b <= c or d <= a:
    print(3)
else:
    print(4)
