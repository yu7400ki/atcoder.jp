def ceil_div(a, b):
    return -(-a // b)

A, B = map(int, input().split())

print(ceil_div(A, B))
