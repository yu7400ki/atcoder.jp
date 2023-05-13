N = int(input())
S = list(input())

a = 0
t = 0

for s in S:
    if s == "A":
        a += 1
        if a >= N // 2:
            print("A")
            break
    else:
        t += 1
        if t >= N // 2:
            print("T")
            break
