import re

N = int(input())
S = input()

if "-" not in S:
    print(-1)
    exit()

S = re.sub(r"-+", "-", S)

if S == "-":
    print(-1)
    exit()

S = S.split("-")

print(len(max(S, key=len)))
