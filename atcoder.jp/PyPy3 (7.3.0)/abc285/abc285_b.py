N = int(input())
S = list(input())

for i in range(1, N):
    ans = 0
    for l in range(1, N - i + 1):
        k = 0
        while k < l and S[k] != S[k + i]:
            k += 1
        ans = max(ans, k)
    print(ans)
