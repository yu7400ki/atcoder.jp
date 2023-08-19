import numpy as np

H, W = map(int, input().split())
c = np.array([list(input()) for _ in range(H)])

while True:
    f = False
    h_deletes = []
    for h in range(H):
        if len(c[h, :]) == 1:
            continue
        if np.all(c[h, :] == c[h, 0]):
            h_deletes.append(h)
            H -= 1
            f = True

    w_deletes = []
    for w in range(W):
        if len(c[:, w]) == 1:
            continue
        if np.all(c[:, w] == c[0, w]):
            w_deletes.append(w)
            W -= 1
            f = True

    i = 0
    for d in h_deletes:
        c = np.delete(c, d - i, 0)
        i += 1

    i = 0
    for d in w_deletes:
        c = np.delete(c, d - i, 1)
        i += 1

    if not f:
        break

print(np.size(c))
