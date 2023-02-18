N = int(input())
S = list(input())

cnt = 0
pre = 0
for s in S:
    if s == "(":
        cnt += 1
    else:
        cnt -= 1
        pre = min(pre, cnt)

if pre < 0:
    S = ["("] * -pre + S
    cnt += -pre

S += [")"] * cnt

print("".join(S))
