N = int(input())
W = input().split()
W[-1] = W[-1][:-1]
T = ['TAKAHASHIKUN','Takahashikun','takahashikun']

cnt = 0
for w in W:
    for t in T:
        if w == t:
            cnt += 1
print(cnt)