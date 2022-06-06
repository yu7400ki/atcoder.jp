N = int(input())
num = [int(input()) for _ in range(5)]

mi = min(num)
group = -(N // -mi) 
print(group + 4)