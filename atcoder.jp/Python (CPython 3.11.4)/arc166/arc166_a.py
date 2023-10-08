def solve(N: int, X: str, Y: str):
    for x, y in zip(X, Y):
        if y == "C" and x != "C":
            return "No"
    Y: list[str] = Y.split("C")
    l = 0
    for y in Y:
        r = l + len(y)
        if l == r:
            l = r + 1
            continue
        ya_idx = []
        xa_idx = []
        for i in range(len(y)):
            if y[i] == "A":
                ya_idx.append(i)
            if X[l + i] == "A":
                xa_idx.append(i)
        for i in range(l, r):
            if len(ya_idx) <= len(xa_idx):
                break
            if X[i] == "C":
                xa_idx.append(i - l)
        if len(xa_idx) != len(ya_idx) or len(ya_idx) != 0 and ya_idx[-1] < max(xa_idx):
            return "No"
        l = r + 1
    return "Yes"


T = int(input())
for _ in range(T):
    N, X, Y = input().split()
    N = int(N)
    ans = solve(N, X, Y)
    print(ans)
