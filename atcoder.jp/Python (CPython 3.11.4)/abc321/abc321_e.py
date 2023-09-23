def search(n, x, k):
    if k < 0:
        return 0
    if len(bin(x)[2:]) + len(bin(k)[2:]) > len(bin(n)[2:]):
        return 0
    left = x << k
    if left > n:
        return 0
    right = left + (1 << k) - 1
    return min(n, right) - left + 1


def solve():
    N, X, K = map(int, input().split())
    ans = search(N, X, K)
    parent = X
    while parent > 1 and K > 0:
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
