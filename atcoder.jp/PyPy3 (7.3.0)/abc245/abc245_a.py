A,B,C,D = map(int,input().split())

t = A * 60 + B
a = C * 60 + D
if t <= a:
    print('Takahashi')
else:
    print('Aoki')