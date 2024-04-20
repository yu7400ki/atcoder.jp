def solve(N, A):
    swaps = []
    for i in range(N):
        min_index = A.index(i + 1)
        if min_index != i:
            swaps.append((i + 1, min_index + 1))
            A[i], A[min_index] = A[min_index], A[i]
    return swaps


N = int(input())
A = list(map(int, input().split()))

swaps = solve(N, A)

print(len(swaps))
for swap in swaps:
    print(*swap)
