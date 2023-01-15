N = int(input())
S = list(input())

for i in range(1, N):
    ans = 0
    for l in range(1, N - i + 1):
        flag = True
        for k in range(1, l + 1):
            if S[k - 1] == S[k + i - 1]:
                flag = False
                break
        if flag:
            ans = max(ans, l)
    print(ans)
