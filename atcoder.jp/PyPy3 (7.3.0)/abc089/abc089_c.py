from collections import defaultdict

N = int(input())

S = defaultdict(int)
for _ in range(N):
    s = input()
    if s[0] in list('MARCH'):
        S[s[0]] += 1

if len(S) <= 2:
    print(0)
    exit()

L = [val for val in S.values()]
print(L)

ans = 0
for i in range(len(S) - 2):
    for j in range(i+1, len(S)-1):
        for k in range(j+1, len(S)):
            ans += L[i] * L[j] * L[k]

print(ans)