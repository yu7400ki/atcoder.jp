N = int(input())

i = 0
while N & 1 == 0:
    N >>= 1
    i += 1

print(i)
