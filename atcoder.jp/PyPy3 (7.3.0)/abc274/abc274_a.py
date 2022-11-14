A, B = map(int, input().split())

def round(x, n):
    x = x * 10 ** n
    x = int(x + 0.5)
    return x / 10 ** n

print(round(B / A, 3))
