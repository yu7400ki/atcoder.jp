a,b,c,d,e,f,x = map(int,input().split())

def jogging(a,b,c,x):
    pos = 0
    while a + c <= x:
        x -= a + c
        pos += a * b
    if x != 0:
        if a <= x:
            pos += a * b
        else:
            pos += x * b
    return pos

if jogging(a,b,c,x) == jogging(d,e,f,x):
    print('Draw')
elif jogging(a,b,c,x) > jogging(d,e,f,x):
    print('Takahashi')
else:
    print('Aoki')