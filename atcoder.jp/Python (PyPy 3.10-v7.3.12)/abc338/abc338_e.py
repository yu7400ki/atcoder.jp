N = int(input())
l = []
pair = {}
for _ in range(N):
    A, B = map(int, input().split())
    a, b = min(A, B), max(A, B)
    l.append(a)
    l.append(b)
    pair[b] = a
l.sort()

stack = []
for i in range(N * 2):
    if not stack:
        stack.append(l[i])
    else:
        if stack[-1] == pair.get(l[i]):
            stack.pop()
        else:
            stack.append(l[i])

if stack:
    print("Yes")
else:
    print("No")
