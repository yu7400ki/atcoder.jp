S = int(input())

X1 = 0
Y1 = 0
X2 = 10**9
Y2 = 1
X3 = (X2 - S % X2) % X2
Y3 = (S + X3) // X2

print(X1, Y1, X2, Y2, X3, Y3)
