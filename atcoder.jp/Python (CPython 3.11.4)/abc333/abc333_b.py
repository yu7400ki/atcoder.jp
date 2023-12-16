S1, S2 = list(input())
T1, T2 = list(input())

if abs(ord(S1) - ord(S2)) == abs(ord(T1) - ord(T2)):
    print("Yes")
else:
    print("No")
