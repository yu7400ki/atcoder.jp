from sys import stdin
input = lambda: stdin.readline().rstrip()

N, Q = map(int,input().split())
S = list(input())

idx = 0
for _ in range(Q):
    i, x = map(int,input().split())
    if i == 1:
        idx = (N - x + idx) % N
    else:
        print(S[(idx+x-1)%N])