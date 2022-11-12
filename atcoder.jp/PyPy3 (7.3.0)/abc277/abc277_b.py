N = int(input())

history = set()

for i in range(N):
    S = input()

    if S[0] not in ["H", "D", "C", "S"]:
        print("No")
        exit()

    if S[1] not in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]:
        print("No")
        exit()

    if S in history:
        print("No")
        exit()

    history.add(S)

print("Yes")