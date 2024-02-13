from functools import lru_cache

@lru_cache(maxsize=None)
def solve(n):
    ret = 0
    if n == 1:
        return ret
    ret += n
    if n % 2 == 0:
        ret += solve(n // 2) * 2
    else:
        ret += solve(n // 2)
        ret += solve(n // 2 + 1)
    return ret

N = int(input())
print(solve(N))
