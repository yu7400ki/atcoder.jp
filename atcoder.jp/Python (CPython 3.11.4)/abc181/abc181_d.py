from collections import Counter

S = input()

if len(S) == 1:
    if int(S) % 8 == 0:
        print("Yes")
    else:
        print("No")
elif len(S) == 2:
    if int(S) % 8 == 0 or int(S[1] + S[0]) % 2 == 0:
        print("Yes")
    else:
        print("No")
else:
    S = Counter(list(S))
    for i in range(0, 1000, 8):
        for k, v in Counter(list(str(i).zfill(3))).items():
            if S[k] < v:
                break
        else:
            print("Yes")
            break
    else:
        print("No")
