class UnionFind():
    # 初期化
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n

    # 根を求める
    def find(self, x):
        if self.par[x] == -1: return x # x が根の場合は x を返す
        else:
            self.par[x] = self.find(self.par[x]) # 経路圧縮
            return self.par[x]

    # x を含むグループと y を含むグループを併合する
    def union(self, x, y):
        # x 側と y 側の根を取得する
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry: return False # すでに同じグループのときは何もしない
        # union by rank
        if self.rank[rx] < self.rank[ry]: # ry 側の rank が小さくなるようにする
            rx, ry = ry, rx
        self.par[ry] = rx # ry を rx の子とする
        if self.rank[rx] == self.rank[ry]: # rx 側の rank を調整する
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry] # rx 側の siz を調整する
        return True

N, M = map(int, input().split())
uf = UnionFind(N)
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    uf.union(u, v)
K = int(input())
par = set()
for _ in range(K):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    par.add((uf.find(x), uf.find(y)))
Q = int(input())
for _ in range(Q):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    par1 = uf.find(p)
    par2 = uf.find(q)
    if (par1, par2) in par or (par2, par1) in par:
        print("No")
    else:
        print("Yes")
