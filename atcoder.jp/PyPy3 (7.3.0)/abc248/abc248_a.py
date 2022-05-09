s = list(map(int,list(input())))
s.sort()
for i in range(9):
    if i != s[i]:
        print(i)
        exit()
print(9)