L1, R1, L2, R2 = map(int,input().split())

print(max(min(R1, R2) - max(L1, L2), 0))