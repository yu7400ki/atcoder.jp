from heapq import heappush, heappop

N, M = map(int, input().split())

ans = [0] * N
wait = []
line = list(range(N))

for _ in range(M):
    T, W, S = map(int, input().split())
    while wait and wait[0][0] <= T:
        t, i = heappop(wait)
        heappush(line, i)
    if not line:
        continue
    i = heappop(line)
    ans[i] += W
    heappush(wait, (T + S, i))

for i in range(N):
    print(ans[i])
