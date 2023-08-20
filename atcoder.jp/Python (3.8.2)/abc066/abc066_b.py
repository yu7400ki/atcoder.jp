S = list(input())

S.pop()
S.pop()

while S[0:len(S) // 2] != S[len(S) // 2:]:
    S.pop()
    S.pop()

print(len(S))
