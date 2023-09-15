from collections import Counter

S = Counter(list(input().zfill(3)))

for i in range(1000):
    if i % 8 != 0:
        continue
    for k, v in Counter(list(str(i).zfill(3))).items():
        if S[k] < v:
            break
    else:
        print("Yes")
        break
else:
    print("No")
