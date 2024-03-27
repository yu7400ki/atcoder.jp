N = int(input())
a, b = sorted(map(int, input().split()))
c, d = sorted(map(int, input().split()))

if (a, b) == (c, d):
    print(2)
elif a < c < b or c < a < d:
    print(4)
else:
    print(3)
