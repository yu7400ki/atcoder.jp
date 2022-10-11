N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

max_odd = -1
max_even = -1
ans = -1

for i in A:
    if i % 2 == 0:
        if max_even == -1:
            max_even = i
        else:
            ans = max(ans, max_even + i)
    elif i % 2 == 1:
        if max_odd == -1:
            max_odd = i
        else:
            ans = max(ans, max_odd + i)

print(ans)
