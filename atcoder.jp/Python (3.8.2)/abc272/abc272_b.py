N, M = map(int,input().split())

def C(n,r):
    ans = 1
    for i in range(n,n-r,-1):
        ans *= i
    for i in range(2,r+1):
        ans //= i
    return ans

combination = set()

for _ in range(M):
    k, *x = map(int,input().split())
    for i in range(k):
        for j in range(i+1,k):
            combination.add((x[i],x[j]))

if C(N,2) == len(combination):
    print("Yes")
else:
    print("No")