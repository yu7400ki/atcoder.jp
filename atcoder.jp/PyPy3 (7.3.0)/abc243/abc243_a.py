V,*ABC = map(int,input().split())

V -= V//sum(ABC) * sum(ABC)
for i in range(3):
    if V < ABC[i]:
        break
    V -= ABC[i]

if i == 0:
    print('F')
elif i == 1:
    print('M')
else:
    print('T')