def solve(N: int, X: str, Y: str):
    for x, y in zip(X, Y):
        if y == "C" and x != "C":
            return "No"
    XC = []
    YC = []
    tmp_x = []
    tmp_y = []
    for x, y in zip(X, Y):
        if y == "C":
            if tmp_y:
                XC.append(tmp_x)
                YC.append(tmp_y)
                tmp_x = []
                tmp_y = []
        else:
            tmp_x.append(x)
            tmp_y.append(y)
    if tmp_y:
        XC.append(tmp_x)
        YC.append(tmp_y)
    if all(solve2(x, y) for x, y in zip(XC, YC)):
        return "Yes"
    else:
        return "No"


def solve2(x: list[str], y: list[str]) -> bool:
    assert len(x) == len(y)
    xa_cnt = x.count("A")
    ya_cnt = y.count("A")
    remain = ya_cnt - xa_cnt
    if remain < 0:
        return False
    for i in range(len(x)):
        if remain > 0 and x[i] == "C":
            x[i] = "A"
            remain -= 1
        elif x[i] == "C":
            x[i] = "B"
    acc_x = [0] * (len(x) + 1)
    acc_y = [0] * (len(y) + 1)
    for i in range(len(x)):
        acc_x[i + 1] = acc_x[i] + (x[i] == "A")
        acc_y[i + 1] = acc_y[i] + (y[i] == "A")
    for a, b in zip(acc_x, acc_y):
        if b > a:
            return False
    return True


T = int(input())
for _ in range(T):
    N, X, Y = input().split()
    N = int(N)
    ans = solve(N, X, Y)
    print(ans)
