N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
num = 0
left = 0
right = 0

while left < N - 1:
    if right == N or num >= K:
        num -= A[left]
        left += 1
    else:
        num += A[right]
        right += 1

    if num >= K:
        ans += N - right + 1

print(ans)
