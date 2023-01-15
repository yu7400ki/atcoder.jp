S = list(input())
N = len(S)

ans = 0
for i in range(len(S)):
    s = S[i]
    j = (ord(s) - ord('A')) * 26 ** (N - i - 1)
    ans += j

for i in range(1, N):
    ans += 26 ** (N - i)

print(ans + 1)
