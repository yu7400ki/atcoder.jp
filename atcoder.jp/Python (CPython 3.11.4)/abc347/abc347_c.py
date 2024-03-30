N, A, B = map(int, input().split())
D = list(map(int, input().split()))
D = [d - D[0] for d in D]

w = A + B

offset = 0
for d in D:
    d %= w
    if d >= A:
        offset = w - d
        if offset >= A:
            print("No")
            break
else:
    print("Yes")
