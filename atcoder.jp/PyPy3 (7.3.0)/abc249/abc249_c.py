from string import ascii_lowercase

n,k = map(int,input().split())
S = [input() for _ in range(n)]

res = 0
for i in range(2**n):
    select = []
    kind = 0
    for j in range(n):
        if (i >> j) & 1:
            select.append(S[j])
    for a in ascii_lowercase:
        cnt = 0
        for s in select:
            if a in s:
                cnt += 1
                if cnt > k:
                    break
        else:
            if cnt == k:
                kind += 1
    res = max(res, kind)

print(res)