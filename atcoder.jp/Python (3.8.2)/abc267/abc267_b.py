S = input()

c = [[7], [4], [8, 2], [5, 1], [9, 3], [6], [10]]

if S[0] == "1":
    print("No")
    exit()

for i in range(7):
    for j in range(i+1, 7):
        stand_flag1 = False
        stand_flag2 = False
        
        for k in c[i]:
            if S[k-1] == "1":
                stand_flag1 = True
        for k in c[j]:
            if S[k-1] == "1":
                stand_flag2 = True
                
        if stand_flag1 and stand_flag2:
            split_flag = False
            
            for k in range(i+1, j):
                cnt = 0
                for l in c[k]:
                    if S[l-1] == "0":
                        cnt += 1
                if cnt == len(c[k]):
                    split_flag = True
                    
            if split_flag:
                print("Yes")
                exit()

print("No")