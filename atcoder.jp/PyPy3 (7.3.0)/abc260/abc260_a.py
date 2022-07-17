from collections import Counter

S = list(input())
S = Counter(S)

for k, v in S.items():
    if v == 1:
        print(k)
        exit()

print(-1)