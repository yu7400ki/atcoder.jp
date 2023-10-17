N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.reverse()
B.reverse()
ans_A = []
ans_B = []
i = 1
while A and B:
    if A[-1] < B[-1]:
        A.pop()
        ans_A.append(i)
    else:
        B.pop()
        ans_B.append(i)
    i += 1

while A:
    A.pop()
    ans_A.append(i)
    i += 1

while B:
    B.pop()
    ans_B.append(i)
    i += 1

print(*ans_A)
print(*ans_B)
