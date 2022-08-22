S = input()

flag = [False] * 26

for s in S:
    flag[ord(s) - ord('a')] = True

for i in range(26):
    if not flag[i]:
        print(chr(ord('a') + i))
        exit()

print('None')