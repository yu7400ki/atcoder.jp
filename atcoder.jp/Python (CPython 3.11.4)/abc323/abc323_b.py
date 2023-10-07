N = int(input())
S = [input() for _ in range(N)]

wins = [s.count("o") for s in S]
wins = [(w, -i) for i, w in enumerate(wins)]
wins.sort(reverse=True)

print(*map(lambda x: -x[1] + 1, wins), sep=" ")
