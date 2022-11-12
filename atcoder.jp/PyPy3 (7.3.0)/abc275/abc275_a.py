N = int(input())
H = list(map(int, input().split()))

ma = max(H)
print(H.index(ma) + 1)
