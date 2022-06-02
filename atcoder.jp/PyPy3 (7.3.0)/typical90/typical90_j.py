N = int(input())
sum_1 = [0] * (N+1)
sum_2 = [0] * (N+1)
for i in range(1, N+1):
    c, p = map(int,input().split())
    if c == 1:
        sum_1[i] = (sum_1[i-1] + p)
        sum_2[i] = (sum_2[i-1])
    elif c == 2:
        sum_1[i] = (sum_1[i-1])
        sum_2[i] = (sum_2[i-1] + p)

Q = int(input())
for _ in range(Q):
    l, r = map(int,input().split())
    ans_1 = sum_1[r] - sum_1[l-1]
    ans_2 = sum_2[r] - sum_2[l-1]
    print(ans_1, ans_2)