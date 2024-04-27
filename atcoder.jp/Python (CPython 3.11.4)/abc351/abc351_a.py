t = sum(map(int, input().split()))
a = sum(map(int, input().split()))
print(max(t - a + 1, 0))