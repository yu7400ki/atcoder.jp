from itertools import permutations

S, K = input().split()
S = list(S)
K = int(K)

ans = list(set(permutations(S)))
ans.sort()

print("".join(ans[K - 1]))
