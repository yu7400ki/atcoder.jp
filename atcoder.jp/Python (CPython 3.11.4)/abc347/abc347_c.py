N, A, B = map(int, input().split())
D = list(map(int, input().split()))

w = A + B
d = [(d - D[0]) % w for d in D]

if all(x < A for x in d):
    print("Yes")
    exit()

rl = min([x % w for x in d if x >= A])
of = w - rl
d = [(x + of) % w for x in d]

if all(x < A for x in d):
    print("Yes")
else:
    print("No")
