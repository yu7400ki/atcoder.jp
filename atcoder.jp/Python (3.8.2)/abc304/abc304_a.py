N = int(input())
name = []
age = []
for _ in range(N):
    a, b = input().split()
    name.append(a)
    age.append(int(b))

min_age = min(age)
min_idx = age.index(min_age)

for i in range(N):
    idx = (min_idx + i) % N
    print(name[idx])
