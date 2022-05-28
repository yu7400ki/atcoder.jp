N, A, B = map(int,input().split())

a = list(range(1,N+1,A))
b = list(range(1,N+1,B))
c = list(range(1,N+1,A*B))
ans = (N * (1+N) // 2) - (len(a) * (A+a[-1]) // 2) - (len(b) * (B+b[-1]) // 2) - (len(c) * (A*B+c[-1]) // 2)

print(ans)