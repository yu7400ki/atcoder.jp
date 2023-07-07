N = int(input())
A = set(map(int, input().split()))
print(len(A) + len(A) % 2 - 1)
