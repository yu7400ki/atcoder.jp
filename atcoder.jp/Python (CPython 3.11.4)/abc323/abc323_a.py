S = input()

ans = True
for i in range(1, 16, 2):
    ans &= S[i] == "0"

if ans:
    print("Yes")
else:
    print("No")
