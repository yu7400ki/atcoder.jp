K = int(input())

if K < 60:
    print(f'21:{str(K).zfill(2)}')
else:
    K -= 60
    print(f'22:{str(K).zfill(2)}')