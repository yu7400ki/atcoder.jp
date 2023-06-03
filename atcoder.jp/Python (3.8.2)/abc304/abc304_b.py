N = input()

if len(N) <= 3:
    print(N)
else:
    print(N[:3] + "0" * (len(N) - 3))
