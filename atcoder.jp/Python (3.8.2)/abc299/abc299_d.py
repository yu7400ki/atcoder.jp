N = int(input())

def q(i):
    print("?", i, flush = True)

def a(p):
    print("!", p, flush = True)

ok = 1
ng = N
for _ in range(20):
    if abs(ok - ng) <= 1:
        break

    i = (ok + ng) // 2
    q(i)
    r = int(input())
    if r == 0:
        ok = i
    else:
        ng = i

a(ok)
