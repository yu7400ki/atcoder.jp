N = int(input())
v = list(map(int, input().split()))

while len(v) > 1:
    mi = float('inf')
    a = 0
    b = 0
    for i in range(len(v)):
        for j in range(i+1, len(v)):
            if abs(v[i] - v[j]) < mi:
                mi = abs(v[i] - v[j])
                a = i
                b = j
    v[a] = (v[a] + v[b]) / 2
    del v[b]

print(v[0])