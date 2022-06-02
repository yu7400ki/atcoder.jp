N = list(input())

ans = 0
for i in range(1, 2**len(N)-1):
    l = []
    r = []
    for j in range(len(N)):
        if i >> j & 1:
            l.append(N[j])
        else:
            r.append(N[j])
    l.sort(reverse=True)
    r.sort(reverse=True)
    ans = max(int(''.join(r)) * int(''.join(l)), ans)
print(ans)