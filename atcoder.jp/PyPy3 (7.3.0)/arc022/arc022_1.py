S = input()
ICT = ['I','C','T']

j = 0
for s in ICT:
    for i in range(j, len(S)):
        if s == S[i].upper():
            j = i
            break
    else:
        print('No')
        exit()
print('Yes')