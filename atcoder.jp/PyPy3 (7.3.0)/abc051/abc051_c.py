sx, xy, tx, ty = map(int, input().split())

ans = ""

x = tx - sx
y = ty - xy

# 1回目の移動
ans += "U" * y
ans += "R" * x

# 2回目の移動
ans += "D" * y
ans += "L" * x

# 3回目の移動
ans += "L"
ans += "U" * (y + 1)
ans += "R" * (x + 1)
ans += "D"

# 4回目の移動
ans += "R"
ans += "D" * (y + 1)
ans += "L" * (x + 1)
ans += "U"

print(ans)
