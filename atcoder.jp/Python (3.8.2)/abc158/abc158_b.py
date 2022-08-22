N, A, B = map(int,input().split())

ans = N // (A + B) * A
ans += min(N - N // (A + B) * (A + B), A)
print(ans)