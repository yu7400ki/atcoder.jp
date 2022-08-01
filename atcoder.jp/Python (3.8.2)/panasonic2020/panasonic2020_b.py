H, W = map(int,input().split())

if W == 1:
    print(1)
    exit()

ans = 0
ans += ((W+1) // 2) * ((H+1) // 2)
ans += (W // 2) * (H // 2)

print(ans)