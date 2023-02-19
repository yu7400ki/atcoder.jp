def solve():
    N, D, K = map(int, input().split())
    K -= 1
    a = 0
    cnt = 0
    history = [a]

    while True:
        walk = (N - a - 1) // D
        cnt += walk
        last = a + walk * D

        if cnt >= K:
            rest = cnt - K
            pos = last - rest * D
            return pos

        a = (last + D) % N
        cnt += 1
        while True:
            flag = True
            for h in history:
                if (a + h) % D == 0: 
                    a += 1
                    flag = False
                    break
            if flag:
                break


T = int(input())

for _ in range(T):
    ans = solve()
    print(ans)
