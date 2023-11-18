import sys
sys.set_int_max_str_digits(0)

N, Q = map(int, input().split())
C = list(map(int, input().split()))

c = [1 << (c - 1) for c in C]
for _ in range(Q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    c[b] |= c[a]
    c[a] = 0
    print(c[b].bit_count())
