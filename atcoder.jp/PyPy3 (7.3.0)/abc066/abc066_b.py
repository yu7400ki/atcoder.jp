S = input()
for i in range(len(S)-2, -1, -2):
    s = S[:i]
    if s[:len(s)//2] == s[len(s)//2:]:
        print(i)
        break