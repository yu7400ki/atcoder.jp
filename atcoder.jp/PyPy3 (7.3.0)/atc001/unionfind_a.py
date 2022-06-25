class UnionFind:
	def __init__(self, n):
		self.n = n
		self.par = [i for i in range(n)]
		self.rank = [0 for i in range(n)]
	def find(self, x):
		if self.par[x] == x:
			return x
		else:
			self.par[x] = self.find(self.par[x])
			return self.par[x]
	def unite(self, x, y):
		x = self.find(x)
		y = self.find(y)
		if x == y: return
		if self.rank[x] < self.rank[y]:
			self.par[x] = y
		else:
			self.par[y] = x
			if self.rank[x] == self.rank[y]:
				self.rank[x] += 1
	def same(self, x, y):
		return self.find(x) == self.find(y)
	def size(self, x):
		return len(self.same(x))
	def count(self):
		return len(self.par)
	def show(self):
		print(self.par)
		print(self.rank)

N, Q = map(int,input().split())
tree = UnionFind(N)
for _ in range(Q):
	P, A, B = map(int,input().split())
	if P == 0:
		tree.unite(A,B)
	elif P == 1:
		if tree.same(A,B):
			print('Yes')
		else:
			print('No')