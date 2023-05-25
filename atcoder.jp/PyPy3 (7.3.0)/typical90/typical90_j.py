N = int(input())

c_1 = [0] * (N + 1)
c_2 = [0] * (N + 1)
for i in range(1, N + 1):
    C, P = map(int, input().split())
    if C == 1:
        c_1[i] = P
    else:
        c_2[i] = P
    c_1[i] += c_1[i - 1]
    c_2[i] += c_2[i - 1]

Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    print(c_1[R] - c_1[L - 1], c_2[R] - c_2[L - 1])
