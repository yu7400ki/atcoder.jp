N = int(input())
S = list(input())

for i in range(N - 1):
    if S[i] == S[i + 1]:
        print("No")
        exit()

print("Yes")
