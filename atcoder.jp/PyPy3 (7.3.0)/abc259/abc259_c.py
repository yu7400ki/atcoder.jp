S = input()
T = input()

len_s = len(S)
len_t = len(T)
if len_t < len_s:
    print('No')
    exit()
elif len_t == len_s:
    print('Yes')
    exit()
else:
    idx_s = 0
    idx_t = 0
    while idx_s < len_s and idx_t < len_t:
        if S[idx_s] != T[idx_t]:
            if S[idx_s-1] == T[idx_t] and S[idx_s-1] == S[idx_s-2]:
                idx_t += 1
            else:
                print('No')
                exit()
        else:
            idx_s += 1
            idx_t += 1
    else:
        print('Yes')
        exit()