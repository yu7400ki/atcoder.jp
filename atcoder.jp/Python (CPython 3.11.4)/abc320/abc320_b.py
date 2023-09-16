S = list(input())
N = len(S)

ans = 0
for l in range(N):
    for r in range(l+1, N+1):
        if S[l:r] == S[l:r][::-1]:
            ans = max(ans, r-l)

print(ans)
