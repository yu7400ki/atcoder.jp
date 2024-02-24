N = int(input())
S = list(input())
Q = int(input())

l = list(range(26))

for i in range(Q):
    c, d = input().split()
    c = ord(c) - ord("a")
    d = ord(d) - ord("a")
    l = [d if x == c else x for x in l]

S = [chr(l[ord(x) - ord("a")] + ord("a")) for x in S]
print("".join(S))
