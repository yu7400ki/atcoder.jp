s = list(map(int,list(input())))
s.sort()
for i in range(10):
    if i != s[i]:
        print(i)
        exit()