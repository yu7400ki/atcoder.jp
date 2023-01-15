N = int(input())
S = list(input())

for i in range(1, N):
    ans = 0
    while ans < (N - i) and S[ans] != S[ans + i]:
        ans += 1
    print(ans)
