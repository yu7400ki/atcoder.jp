from string import ascii_lowercase

n,k = map(int,input().split())
S = [set(input()) for _ in range(n)]

res = []
for i in range(1,2**n):
    select = []
    for j in range(n):
        if (i >> j) & 1:
            select.append(S[j])
    memo = []
    for a in ascii_lowercase:
        cnt = 0
        for s in select:
            if a in s:
                cnt += 1
        memo.append(cnt)
    memo = list(filter(lambda x:x == k,memo))
    res.append(len(memo))

print(max(res))