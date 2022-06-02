N = int(input())

s = set()
for i in range(2,int(N**0.5)+1):
    for j in range(2,int(N**0.5)+1):
        a = i**j
        if a > N:
            break
        s.add(a)
    
print(N - len(s))