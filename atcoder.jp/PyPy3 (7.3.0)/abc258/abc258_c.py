from sys import stdin
input = lambda: stdin.readline().rstrip()

N, Q = map(int,input().split())
S = list(input())


for _ in range(Q):
    i, x = map(int,input().split())
    if i == 1:
        S = S[-x:] + S[:-x]
    else:
        print(S[x-1])