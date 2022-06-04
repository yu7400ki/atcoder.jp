S = input()

red = S.count('0')
blue = S.count('1')

print(len(S) - abs(red-blue))