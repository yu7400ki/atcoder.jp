S = list(input())
N = len(S)

atcoder = "atcoder"
ans = 0
for i in range(N):
    for j in range(N - i - 1):
        if atcoder.index(S[j]) > atcoder.index(S[j + 1]):
            S[j], S[j + 1] = S[j + 1], S[j]
            ans += 1

print(ans)
