N = int(input())
A = list(map(lambda x: int(x) - 1, input().split()))

called = [False] * N

for i in range(N):
    if called[i]:
        continue

    called[A[i]] = True

ans = list(map(lambda x: x + 1, filter(lambda x: not called[x], range(N))))

print(len(ans))
print(*ans, sep=" ")
