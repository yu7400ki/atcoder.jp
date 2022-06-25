class UnionFind:
	def __init__(self, n):
		self.n = n
		self.parent = [i for i in range(n)]
		self.size = [1 for _ in range(n)]
	def find(self, x):
		if self.parent[x] == x:
			return x
		else:
			self.parent[x] = self.find(self.parent[x])
			return self.parent[x]
	def union(self, x, y):
		x = self.find(x)
		y = self.find(y)
		if x == y: return
		if self.size[x] > self.size[y]:
			self.parent[y] = x
			self.size[x] += self.size[y]
		else:
			self.parent[x] = y
			self.size[y] += self.size[x]
	def same(self, x, y):
		return self.find(x) == self.find(y)
	def count(self):
		return len(set(self.parent))
	def size(self, x):
		return self.size[self.find(x)]

N, M = map(int,input().split())
uf = UnionFind(N)
for _ in range(M):
	A, B = map(int,input().split())
	uf.union(A-1,B-1)

print(uf.count()-1)