N = int(input())
a = list(map(int, input().split()))

memo = []
ans = 0
for j in range(N):
    if a[j] == j+1:
        ans += len(memo)
        memo.append(j+1)
    else:
        i = a[j] - 1
        if i < j:
            if (min(a[i], a[j]) == i+1) and (max(a[i], a[j]) == j+1):
                ans += 1

print(ans)