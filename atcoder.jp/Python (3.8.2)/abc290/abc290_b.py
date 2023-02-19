N, K = map(int, input().split())
S = list(input())

cnt = 0
ans = []
for s in S:
    if s == "o":
        if cnt < K:
            cnt += 1
            ans.append(s)
        else:
            ans.append("x")
    else:
        ans.append(s)

print("".join(ans))
