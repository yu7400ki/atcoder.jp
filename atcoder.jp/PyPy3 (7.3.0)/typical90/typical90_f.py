from string import ascii_lowercase as al

N, K = map(int, input().split())
S = list(input())

idx = 0
ans = []
for _ in range(K):
    for char in al:
        for i in range(idx, N - K + len(ans) + 1):
            if S[i] == char:
                ans.append(char)
                idx = i + 1
                break
        else:
            continue
        break

print(''.join(ans))
