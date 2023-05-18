N = int(input())


for bit in range(2 ** N):
    cnt = 0
    for i in range(N):
        if bit << i & 1 << N - 1:
            cnt -= 1
        else:
            cnt += 1
        if cnt < 0:
            break
    else:
        if cnt != 0:
            continue
        ans = ""
        for i in range(N):
            if bit << i & 1 << N - 1:
                ans += ")"
            else:
                ans += "("
        print(ans)
