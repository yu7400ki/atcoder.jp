N, M = map(int,input().split())

group = []
not_seen = set(range(1,N+1))
for _ in range(M):
	A, B = map(int,input().split())
	not_seen.discard(A)
	not_seen.discard(B)
	for g in group:
		if A in g or B in g:
			g.add(A)
			g.add(B)
	else:
		group.append(set())
		group[-1].add(A)
		group[-1].add(B)

print(len(group)-1 + len(not_seen))