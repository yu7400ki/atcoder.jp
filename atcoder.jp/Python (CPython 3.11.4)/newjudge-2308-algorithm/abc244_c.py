def say(x):
    print(x, flush=True)
    res = int(input())
    if res == 0:
        exit()
    return res


N = int(input())

remain = set(x for x in range(1, 2 * N + 2))

while remain:
    x = next(iter(remain))
    remain.discard(x)
    res = say(x)
    remain.discard(res)
