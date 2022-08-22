A, B = map(int,input().split())
S = input()

if S[A] == '-':
    if S.count('-') == 1:
        print('Yes')
        exit()

print('No')