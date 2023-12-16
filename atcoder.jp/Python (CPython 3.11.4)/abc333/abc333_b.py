S1, S2 = list(input())
T1, T2 = list(input())

d1 = abs(ord(S1) - ord(S2))
d2 = abs(ord(T1) - ord(T2))

if d1 > 2:
    d1 = 5 - d1
if d2 > 2:
    d2 = 5 - d2

if d1 == d2:
    print("Yes")
else:
    print("No")
