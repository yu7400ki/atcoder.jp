import random

S = list(input().split())
T = list(input().split())

cnt = 0

while S != T:
    cnt += 1
    i = random.randint(0, 2)
    j = random.randint(0, 2)
    S[i], S[j] = S[j], S[i]

if cnt % 2 == 0:
    print("Yes")
else:
    print("No")
