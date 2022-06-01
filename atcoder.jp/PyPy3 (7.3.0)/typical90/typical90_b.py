from collections import deque

N = int(input())

for i in range(2**N):
    l = deque()
    cnt1 = 0
    cnt2 = 0
    s = ''
    for j in range(N):
        l.appendleft(i>>j&1)
    for n in l:
        if n == 0:
            cnt1 += 1
            s += '('
        else:
            cnt2 += 1
            s += ')'
        if cnt1 < cnt2:
            break
    else:
        if cnt1 == cnt2:
            print(s)