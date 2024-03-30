N, A, B = map(int, input().split())
D = list(map(int, input().split()))
D = [d - D[0] for d in D]

w = A + B

ans = 0
for d, e in zip(D, D[1:]):
    d += ans
    e += ans
    if (e - d) % w < A:
        continue
    else:
        ans = w - e
        if ans >= A:
            print("No")
            break
else:
    print("Yes")
