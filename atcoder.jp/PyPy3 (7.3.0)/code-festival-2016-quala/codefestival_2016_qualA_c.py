S = list(input())
K = int(input())

for i, s in enumerate(S):
    d = (123 - ord(s)) % 26
    if d <= K:
        S[i] = "a"
        K -= d

if K != 0:
    S[-1] = chr(ord(S[-1]) + K % 26)

print(*S, sep="")
