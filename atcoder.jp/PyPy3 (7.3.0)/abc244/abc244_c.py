N = int(input())
limit = 2 * N + 1

seen = set()
for i in range(N+1):
    for j in range(1,limit+1):
        if j not in seen:
            print(j)
            seen.add(j)
            break
    n = int(input())
    if n == 0:
        exit()
    seen.add(n)