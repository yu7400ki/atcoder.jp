A = [int(input()) for _ in range(5)]

lst1 = list(filter(lambda x: x % 10 == 0, A))
last, *lst2 = sorted(filter(lambda x: x % 10 != 0, A), key=lambda x: x % 10)

ans = sum(lst1) + sum(map(lambda x: x + 10 - x % 10, lst2)) + last

print(ans)
