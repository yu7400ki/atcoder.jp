dist = [3, 1, 4, 1, 5, 9]
acc = [0]
for i in range(len(dist)):
    acc.append(acc[i] + dist[i])

p, q = input().split()
i = ord(p) - ord("A")
j = ord(q) - ord("A")

print(abs(acc[j] - acc[i]))
