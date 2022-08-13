R, C = map(int,input().split())

table = [[''] * 15 for _ in range(15)]

for i in range(8):
    for j in range(-i, i+1):
        for k in range(-i, i+1):
            if table[j+7][k+7] != '': continue
            table[j+7][k+7] = 'white' if i % 2 == 0 else 'black'

print(table[R-1][C-1])