H1, W1 = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H1)]
H2, W2 = map(int,input().split())
B = [list(map(int,input().split())) for _ in range(H2)]

from itertools import combinations
from copy import deepcopy

H = H1 - H2
W = W1 - W2

for del_h in combinations(range(H1), H):
    for del_w in combinations(range(W1), W):
        A_copy = deepcopy(A)
        for i, el in enumerate(del_h):
            A_copy.pop(el-i)
        for i, el in enumerate(del_w):
            for j in range(len(A_copy)):
                A_copy[j].pop(el-i)
        if A_copy == B:
            print('Yes')
            exit()

print('No')