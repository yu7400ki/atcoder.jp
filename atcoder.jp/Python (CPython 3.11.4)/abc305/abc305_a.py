N = int(input())

ans = min([x for x in range(0, 101, 5)], key=lambda x: abs(x - N))

print(ans)
