S = list(input())

for i in range(len(S)):
    if S[i] == 'a': S[i] = 0
    if S[i] == 't': S[i] = 1
    if S[i] == 'c': S[i] = 2
    if S[i] == 'o': S[i] = 3
    if S[i] == 'd': S[i] = 4
    if S[i] == 'e': S[i] = 5
    if S[i] == 'r': S[i] = 6

cnt = 0

for i in range(len(S)):
    for j in range(len(S)-i-1):
        if S[j] > S[j+1]:
            cnt += 1
            S[j], S[j+1] = S[j+1], S[j]

print(cnt)