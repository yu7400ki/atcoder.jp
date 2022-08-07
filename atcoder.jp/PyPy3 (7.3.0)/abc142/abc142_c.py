N = int(input())
A = [(i+1, x) for i, x in enumerate(map(int, input().split()))]

A.sort(key=lambda x: x[1])

print(' '.join(map(lambda x: str(x[0]), A)))