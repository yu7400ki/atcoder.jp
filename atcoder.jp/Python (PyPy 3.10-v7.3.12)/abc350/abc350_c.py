N = int(input())
A = list(map(int, input().split()))

def solve(N, A):
    index_map = {a: i for i, a in enumerate(A)}
    swaps = []
    for i in range(N):
        min_index = index_map[i + 1]
        if min_index != i:
            swaps.append((i + 1, min_index + 1))
            A[i], A[min_index] = A[min_index], A[i]
            index_map[A[i]] = i
            index_map[A[min_index]] = min_index
    return swaps

swaps = solve(N, A)

print(len(swaps))
for swap in swaps:
    print(*swap)
