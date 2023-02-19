from collections import deque

N, K = map(int, input().split())
A = list(map(int, input().split()))

lst = deque(sorted(A))

if lst[0] != 0:
    print(0)
    exit()

res = [lst.popleft()]
rest = []

while True:
    a = lst.popleft()
    if a == res[-1]:
        rest.append(a)
    elif a == res[-1] + 1:
        res.append(a)
    else:
        res.append(a)
        while len(res) != K:
            if rest:
                res.append(rest.pop())
            else:
                res.append(lst.pop())
    if len(res) == K:
        break

for i in range(K - 1):
    if res[i] + 1 != res[i + 1]:
        break
else:
    i += 1

if i + 1 not in res:
    print(i + 1)
else:
    print(0)
