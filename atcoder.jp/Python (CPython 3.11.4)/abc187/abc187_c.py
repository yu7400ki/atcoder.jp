N = int(input())
S = [input() for _ in range(N)]

a = set()
b = set()

for s in S:
    if s.startswith("!"):
        a.add(s[1:])
    else:
        b.add(s)

c = a & b
if c:
    print(c.pop())
else:
    print("satisfiable")
