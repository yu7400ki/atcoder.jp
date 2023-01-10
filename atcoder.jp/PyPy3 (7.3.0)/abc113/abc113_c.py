N, M = map(int, input().split())
PY = [tuple(map(int, input().split())) for _ in range(M)]

sortedPY = sorted(PY, key = lambda py: py[1])
counter = [0] * (N + 1)
ans = {}

for p, y in sortedPY:
    counter[p] += 1
    ans[y] = f"{p:06}{counter[p]:06}"

for _, y in PY:
    print(ans[y])
