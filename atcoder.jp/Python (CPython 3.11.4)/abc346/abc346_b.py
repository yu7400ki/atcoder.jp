from collections import deque

W, B = map(int, input().split())

s = deque()
cnt = {"w": 0, "b": 0}

for i in range(100):
    for p in list("wbwbwwbwbwbw"):
        s.append(p)
        cnt[p] += 1
        if len(s) > W + B:
            cnt[s.popleft()] -= 1
        if cnt["w"] == W and cnt["b"] == B:
            print("Yes")
            exit()
print("No")
