S = list(input())

o = ord("a")
cnt = [0] * 26

for s in S:
    cnt[ord(s) - o] += 1

i = cnt.index(max(cnt))

print(chr(i + o))
