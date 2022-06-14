N = int(input())
S = input()

if N % 2:
    print(-1)
else:
    cnt = 0
    for i in range(N//2):
        if S[i] != S[i+N//2]:
            cnt += 1
    print(cnt)