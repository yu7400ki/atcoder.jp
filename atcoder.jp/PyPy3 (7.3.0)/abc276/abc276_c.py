from itertools import permutations

N = int(input())
P = list(map(int,input().split()))

prev = []
for iter in permutations(range(1,N+1)):
    if list(iter) == P:
        print(*prev)
        break

    prev = iter
