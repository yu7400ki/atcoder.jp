from collections import Counter

S = list(input())
T = list(input())

can_replace = ["a", "t", "c", "o", "d", "e", "r"]

s = Counter(S)
t = Counter(T)

if "@" not in s:
    s["@"] = 0
if "@" not in t:
    t["@"] = 0

visited = set(["@"])

for l, r in zip([s, t], [t, s]):
    for key in l.keys():
        if key in visited:
            continue
        visited.add(key)
        if key in r:
            if r[key] == l[key]:
                continue
            elif r[key] > l[key]:
                if key not in can_replace:
                    print("No")
                    exit()
                l["@"] -= r[key] - l[key]
                if l["@"] < 0:
                    print("No")
                    exit()
            else:
                if key not in can_replace:
                    print("No")
                    exit()
                r["@"] -= l[key] - r[key]
                if r["@"] < 0:
                    print("No")
                    exit()
        else:
            if key not in can_replace:
                print("No")
                exit()
            r["@"] -= l[key]
            if r["@"] < 0:
                print("No")
                exit()

print("Yes")
