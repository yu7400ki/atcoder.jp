def search(n, x, k):
    if k < 0:
        return 0
    left = x << k
    right = left + (1 << k) - 1
    if left > n:
        return 0
    else:
        return min(n, right) - left + 1


def solve():
    N, X, K = map(int, input().split())
    ans = search(N, X, K)
    parent = X
    while parent != 1 and K > 0:
        opposite = parent ^ 1
        parent = parent >> 1
        K -= 1
        if K == 0:
            ans += 1
            break
        d = K - 1
        ans += search(N, opposite, d)
    print(ans)


T = int(input())
for i in range(T):
    solve()
