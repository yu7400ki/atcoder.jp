K = int(input())

lunlun = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
next = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
while True:
    tmp = []
    for n in next:
        if n[-1] != "0":
            tmp.append(n + str(int(n[-1]) - 1))
        tmp.append(n + n[-1])
        if n[-1] != "9":
            tmp.append(n + str(int(n[-1]) + 1))
    lunlun.extend(tmp)
    next = tmp
    if len(lunlun) >= K:
        break

print(lunlun[K-1])
