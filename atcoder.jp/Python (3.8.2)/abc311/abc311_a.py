N = int(input())
S = list(input())

flag = [False] * 3

for i in range(N):
    flag[ord(S[i]) - ord("A")] = True
    if all(flag):
        break

print(i + 1)
