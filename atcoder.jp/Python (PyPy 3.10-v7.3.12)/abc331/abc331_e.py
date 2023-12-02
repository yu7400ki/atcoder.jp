from collections import defaultdict

N, M, L = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

pair = defaultdict(set)
for _ in range(L):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    pair[c].add(d)

a_sorted = sorted(enumerate(a), key=lambda x: x[1], reverse=True)
b_sorted = sorted(enumerate(b), key=lambda x: x[1], reverse=True)

ans = -1
for i, a in a_sorted:
    for j, b in b_sorted:
        if j in pair[i]:
            continue
        else:
            ans = max(ans, a + b)
            break

print(ans)
