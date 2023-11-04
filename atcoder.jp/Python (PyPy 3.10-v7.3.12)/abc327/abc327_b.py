B = int(input())

i = 0
while B > i ** i:
    i += 1

if B == i ** i:
    print(i)
else:
    print(-1)
