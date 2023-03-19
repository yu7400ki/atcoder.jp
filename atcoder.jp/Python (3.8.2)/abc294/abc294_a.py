N = int(input())
A = list(map(int, input().split()))

ans = list(filter(lambda x: x % 2 == 0, A))

print(*ans, sep=' ')
