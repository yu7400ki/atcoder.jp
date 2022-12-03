N = int(input())
S = list(map(int,input().split()))

ans = [0] * N
ans[0] = S[0]

for i in range(1, N):
    ans[i] = S[i] - sum(ans[:i])

print(*ans)