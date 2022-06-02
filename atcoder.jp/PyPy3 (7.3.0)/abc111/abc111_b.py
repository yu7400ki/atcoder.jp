N = int(input())

for i in range(N//100, 11):
    ABC = int(str(i) * 3)
    if ABC >= N:
        print(ABC)
        exit()