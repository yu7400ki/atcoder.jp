a, b, C = map(int, input().split())
c = C.bit_count()

for i in range(c + 1):
    j = c - i
    x = a - i
    y = b - j
    if x == y and x >= 0 and y >= 0:
        k = 1
        X = 0
        Y = 0
        while i or j or x:
            if C & k:
                if i:
                    i -= 1
                    X |= k
                elif j:
                    j -= 1
                    Y |= k
            else:
                if x:
                    x -= 1
                    X |= k
                    Y |= k
            k <<= 1
        if X < 1 << 60 and Y < 1 << 60:
            assert X ^ Y == C
            assert X.bit_count() == a
            assert Y.bit_count() == b
            print(X, Y)
            break
else:
    print(-1)
