from collections import defaultdict, deque

def fastio(f):
    import builtins, functools, io, os, sys

    buf = io.BytesIO()
    builtin_print = builtins.print
    builtin_input = builtins.input

    def fast_print(arg, *args, sep=" ", end="\n", **_):
        sep = sep.encode()
        end = end.encode()
        buf.write(str(arg).encode())
        for arg in args:
            buf.write(sep)
            buf.write(str(arg).encode())
        buf.write(end)

    def fast_input():
        return sys.stdin.readline().rstrip()

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        builtins.print = fast_print
        builtins.input = fast_input
        res = f(*args, **kwargs)
        os.write(1, buf.getvalue())
        buf.seek(0)
        buf.truncate(0)
        builtins.print = builtin_print
        builtins.input = builtin_input
        return res

    return wrapper

def bfs(graph, n, limit):
    dic = defaultdict(lambda : -1)
    queue = deque()
    queue.append(n)
    dic[n] = 0
    ans = n
    while len(queue) != 0:
        pos = queue.popleft()
        for i in graph[pos]:
            if dic[i] == -1:
                dic[i] = dic[pos] + 1
                if dic[i] <= limit:
                    ans += i
                    if dic[i] < limit:
                        queue.append(i)
    return ans

@fastio
def solve():
    N, M = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    Q = int(input())

    for _ in range(Q):
        x, k = map(int, input().split())
        ans = bfs(graph, x, k)
        print(ans)

if __name__ == "__main__":
    solve()
