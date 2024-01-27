N = int(input())
l = []
r = []
for _ in range(N):
    a, b = map(int, input().split())
    l.append(min(a, b))
    r.append(max(a, b))

h = l + r
h.sort(reverse=True)
r = {x: y for x, y in zip(r, l)}
l = set(l)

stack = []
while h:
    x = h.pop()
    if x in l:
        stack.append(x)
    else:
        if stack and stack[-1] == r[x]:
            stack.pop()
        else:
            print("Yes")
            break
else:
    print("No")
