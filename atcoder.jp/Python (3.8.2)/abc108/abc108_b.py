x1, y1, x2, y2, = map(int, input().split())

vec1 = [x2 - x1, y2 - y1]
vec1[0], vec1[1] = -vec1[1], vec1[0]
p4 = [x1 + vec1[0], y1 + vec1[1]]

vec2 = [x1 - x2, y1 - y2]
vec2[0], vec2[1] = vec2[1], -vec2[0]
p3 = [x2 + vec2[0], y2 + vec2[1]]

print(*p3, *p4)