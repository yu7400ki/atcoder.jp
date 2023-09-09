N = int(input())

ans = []

for i in range(N+1):
    for j in range(1, 10):
        if N % j != 0:
            continue
        else:
            if i % (N // j) == 0:
                ans.append(str(j))
                break
    else:
        ans.append("-")

print("".join(ans))
