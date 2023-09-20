N, K = map(int, input().split())
V = list(map(int, input().split()))

ans = 0
for l in range(N+1):
    for r in range(N+1):
        n = K - l - r
        if n < 0:
            break
        get = []
        for i in range(l):
            get.append(V[i])
        for j in range(r):
            get.append(V[N - j - 1])
        get.sort(reverse=True)
        while get and get[-1] < 0 and n > 0:
            get.pop()
            n -= 1
        tmp = sum(get)
        ans = max(ans, tmp)

print(ans)
