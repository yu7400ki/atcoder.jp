def check(T: str, S: str) -> bool:
    if T == S:
        return True
    elif len(T) == len(S):
        diff = 0
        for t, s in zip(T, S):
            if t != s:
                diff += 1
        if diff == 1:
            return True
    elif len(T) == len(S) + 1:
        i, j = 0, 0
        while i < len(T) and j < len(S):
            if T[i] == S[j]:
                i += 1
                j += 1
            else:
                i += 1
        if j == len(S):
            return True
    elif len(T) + 1 == len(S):
        return check(S, T)
    return False


N, T = input().split()
N = int(N)

ans = []
for i in range(N):
    S = input()
    if check(T, S):
        ans.append(i + 1)

print(len(ans))
print(*ans, sep=" ")
