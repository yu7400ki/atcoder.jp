import io, os
buf = io.BytesIO()
def print(*args, sep=" ", end="\n"):
    for arg in args:
        buf.write(str(arg).encode())
        buf.write(sep.encode())
    buf.write(end.encode())

def solve():
    from collections import Counter

    N = int(input())
    A = list(map(int, input().split()))

    count = Counter(A)
    for i in sorted(list(set(A)), reverse=True):
        print(count[i])
    for _ in range(N - len(count)):
        print(0)

if __name__ == "__main__":
    solve()
    os.write(1, buf.getvalue())
