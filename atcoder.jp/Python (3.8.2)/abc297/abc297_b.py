S = input()

x = S.find("B")
y = S.rfind("B")

if x % 2 == y % 2:
    print("No")
    exit()

x = S.find("R")
y = S.rfind("R")
k = S.find("K")

if not x < k < y:
    print("No")
    exit()

print("Yes")
