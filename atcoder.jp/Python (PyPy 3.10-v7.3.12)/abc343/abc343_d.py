N, T = map(int, input().split())

scr = [0] * N
cnt = {0: N}

for i in range(T):
    A, B = map(int, input().split())
    A -= 1
    cnt[scr[A]] -= 1
    if cnt[scr[A]] == 0:
        cnt.pop(scr[A])
    scr[A] += B
    cnt[scr[A]] = cnt.get(scr[A], 0) + 1
    print(len(cnt))
