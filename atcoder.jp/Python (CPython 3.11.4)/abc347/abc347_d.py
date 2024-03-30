a, b, C = map(int, input().split())
c = C.bit_count()

for i in range(c):
    j = c - i
    x = a - i
    y = b - j
    if x == y and x >= 0 and y >= 0:
        k = 1
        ans_a = 0
        ans_b = 0
        while i or j or x:
            if C & k:
                if i:
                    i -= 1
                    ans_a |= k
                elif j:
                    j -= 1
                    ans_b |= k
            else:
                if x:
                    x -= 1
                    ans_a |= k
                    ans_b |= k
            k <<= 1
        if ans_a < 1 << 60 - 1 and ans_b < 1 << 60 - 1:
            print(ans_a, ans_b)
            assert ans_a ^ ans_b == C
            assert ans_a.bit_count() == a
            assert ans_b.bit_count() == b
            break
else:
    print(-1)
