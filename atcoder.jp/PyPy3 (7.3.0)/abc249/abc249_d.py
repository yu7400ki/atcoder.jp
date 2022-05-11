from collections import Counter

N = int(input())
A = list(map(int,input().split()))
cnt = Counter(A)

def f(x):
    res = []
    for i in range(1,int(x**0.5)+1):
        if x % i == 0:
            j = x // i
            res.append((i,j))
            if i != j:
                res.append((j,i))
    return res

ans = 0
for ai in A:
    for aj, ak in f(ai):
    	ans += cnt[aj] * cnt[ak]
    
print(ans)