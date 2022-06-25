from string import ascii_uppercase

N, X = map(int,input().split())
S = [s for s in ascii_uppercase for _ in range(N)]

print(S[X-1])