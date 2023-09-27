from collections import deque

N, M = map(int, input().split())
A = []
for _ in range(M):
    input()
    a = list(map(int, input().split()))[::-1]
    A.append(a)

counter = {1: set(), 2: set()}
pos = {i: [] for i in range(N)}

for i, a in enumerate(A):
    t = a[-1] - 1
    pos[t].append(i)
    if t in counter[1]:
        counter[1].remove(t)
        counter[2].add(t)
    else:
        counter[1].add(t)

while counter[2]:
    a = counter[2].pop()
    while pos[a]:
        i = pos[a].pop()
        A[i].pop()
        if A[i]:
            t = A[i][-1] - 1
            pos[t].append(i)
            if t in counter[1]:
                counter[1].remove(t)
                counter[2].add(t)
            else:
                counter[1].add(t)

if all(len(a) == 0 for a in A):
    print("Yes")
else:
    print("No")
