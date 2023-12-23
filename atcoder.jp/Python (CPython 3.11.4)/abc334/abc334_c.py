N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
if K % 2 == 0:
    for i in range(0, K, 2):
        ans += A[i + 1] - A[i]
else:
    import heapq
    q = []
    for i in range(K - 1):
        heapq.heappush(q, (A[i + 1] - A[i], i, i + 1))
    ans = 0
    s = set()
    while len(s) < K - 1:
        d, i, j = heapq.heappop(q)
        if i in s or j in s:
            continue
        ans += d
        s.add(i)
        s.add(j)

print(ans)
