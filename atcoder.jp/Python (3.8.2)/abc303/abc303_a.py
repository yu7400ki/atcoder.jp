N = int(input())
S = input()
T = input()

S = S.replace("1", "l").replace("0", "o")
T = T.replace("1", "l").replace("0", "o")

for s, t in zip(S, T):
    if s != t:
        print("No")
        exit()
print("Yes")
