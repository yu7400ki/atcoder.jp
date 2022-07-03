K = int(input())

if K < 60:
    print(f'21:{K:02d}')
else:
    K -= 60
    print(f'22:{K:02d}')