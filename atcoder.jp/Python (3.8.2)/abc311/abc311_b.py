N, D = map(int, input().split())

flag = [1] * D

for _ in range(N):
    S = list(input())
    for i, s in enumerate(S):
        flag[i] &= int(s == "o")

print(max(map(len, "".join(map(str, flag)).split("0"))))
