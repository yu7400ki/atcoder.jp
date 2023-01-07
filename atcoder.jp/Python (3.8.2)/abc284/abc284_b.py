def solve(n, a):
    return sum([x % 2 for x in a])


T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    ans = solve(N, A)
    print(ans)
