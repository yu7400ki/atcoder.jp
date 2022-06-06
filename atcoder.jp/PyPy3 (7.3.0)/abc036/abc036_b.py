N = int(input())
s = [list(input()) for _ in range(N)]

for x in zip(*s[::-1]):
    print(''.join(x))