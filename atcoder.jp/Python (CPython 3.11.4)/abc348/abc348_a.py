N = int(input())
print(*["x" if i % 3 == 0 else "o" for i in range(1, N + 1)], sep="")
