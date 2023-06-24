N = int(input())
S = [input() for _ in range(N)]

for i in range(N):
    for j in range(i+1, N):
        s = S[i] + S[j]
        if s == s[::-1]:
            print("Yes")
            exit()
        s = S[j] + S[i]
        if s == s[::-1]:
            print("Yes")
            exit()

print("No")
