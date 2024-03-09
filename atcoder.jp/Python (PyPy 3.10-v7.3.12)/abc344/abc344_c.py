N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = set(map(int, input().split()))
L = int(input())
C = set(map(int, input().split()))
Q = int(input())
X = list(map(int, input().split()))

s = set()
for a in A:
    for b in B:
        for c in C:
            s.add(a + b + c)

for x in X:
    if x in s:
        print("Yes")
    else:
        print("No")
