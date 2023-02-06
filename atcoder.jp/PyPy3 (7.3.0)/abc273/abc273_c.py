def fastout(f):
    import builtins, functools, io, os

    buf = io.BytesIO()
    builtin_print = builtins.print

    def fast_print(arg, *args, sep=" ", end="\n", **_):
        sep = sep.encode()
        end = end.encode()
        buf.write(str(arg).encode())
        for arg in args:
            buf.write(sep)
            buf.write(str(arg).encode())
        buf.write(end)

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        builtins.print = fast_print
        res = f(*args, **kwargs)
        os.write(1, buf.getvalue())
        buf.seek(0)
        buf.truncate(0)
        builtins.print = builtin_print
        return res

    return wrapper

@fastout
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
