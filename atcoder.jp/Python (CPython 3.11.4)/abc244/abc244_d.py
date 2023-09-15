import random

S = list(input().split())
T = list(input().split())

cnt = 0

while S != T:
    i = random.randint(0, 2)
    j = random.randint(0, 2)
    if i == j:
        continue
    cnt += 1
    S[i], S[j] = S[j], S[i]

if cnt % 2 == 0:
    print("Yes")
else:
    print("No")
