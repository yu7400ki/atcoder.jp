s = input()

if len(s) == len(set(s)):
    if s.islower() or s.isupper():
        print('No')
    else:
        print('Yes')
else:
    print('No')