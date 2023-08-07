from collections import defaultdict

N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]
S = list(input())

person_r = defaultdict(list)
person_l = defaultdict(list)

for s, (x, y) in zip(S, XY):
    if s == "R":
        person_r[y].append(x)
    else:
        person_l[y].append(x)

y = set(person_r.keys()) & set(person_l.keys())

for key in y:
    person_r[key].sort()
    person_l[key].sort()

for key in y:
    if person_r[key][0] < person_l[key][-1]:
        print("Yes")
        break
else:
    print("No")
