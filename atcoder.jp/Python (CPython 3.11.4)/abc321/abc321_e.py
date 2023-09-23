def solve():
    N, X, K = map(int, input().split())
    left = X << K
    right = left + (1 << K) - 1
    if left > N:
        ans = 0
    else:
        ans = min(N, right) - left + 1
    parent = X
    while parent != 1 and K > 0:
        K -= 1
        if K == 0:
            ans += 1
            break
        b = bin(parent)[2:]
        parent = parent >> 1
        d = K - 1
        if b[-1] == "0":
            root = (parent << 1) + 1
        else:
            root = parent << 1
        left = root << d
        right = left + (1 << d) - 1
        if left > N:
            ans += 0
        else:
            ans += min(N, right) - left + 1
    print(ans)


T = int(input())
for i in range(T):
    solve()
