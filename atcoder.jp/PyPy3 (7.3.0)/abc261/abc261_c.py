from collections import defaultdict

counter = defaultdict(int)
N = int(input())
for _ in range(N):
    S = input()
    if counter[S] > 0:
        print(f'{S}({counter[S]})')
    else:
        print(S)
    counter[S] += 1