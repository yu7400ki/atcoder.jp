from collections import defaultdict

N, Q = map(int,input().split())

follow = [set() for _ in range(N)]
follower = [set() for _ in range(N)]

for _ in range(Q):
    queue = list(map(int,input().split()))
    if queue[0] == 1:
        a = queue[1]; b = queue[2]
        a -= 1; b -= 1
        follow[a].add(b)
        follower[b].add(a)
    if queue[0] == 2:
        a = queue[1]
        a -= 1
        follow[a] |= follower[a]
        followers = list(follower[a])
        for f in followers:
            follower[f].add(a)
    if queue[0] == 3:
        a = queue[1]
        a -= 1
        follows = list(follow[a])
        for f in follows:
            follow[a] |= follow[f]
            follows = list(follow[f])
            for f in follows:
                follower[f].add(a)
            follow[a].discard(a)

for i in range(N):
    for j in range(N):
        if j in follow[i]:
            print('Y', end='')
        else:
            print('N', end='')
    print()