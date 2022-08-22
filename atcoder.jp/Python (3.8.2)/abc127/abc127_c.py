N, M = map(int,input().split())

cards = [0] * (N+1)
for i in range(M):
    L, R = map(int,input().split())
    cards[L-1] += 1
    cards[R] -= 1

def accumulate(l):
    res = [0] * (len(l) + 1)
    for i, n in enumerate(l):
        res[i+1] = res[i] + n
    return res

ans = 0
cards = accumulate(cards)
for i in cards:
    if i == M:
        ans += 1

print(ans)