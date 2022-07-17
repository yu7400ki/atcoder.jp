N, X, Y = map(int,input().split())

red = [0] * N
blue = [0] * N
red[-1] = 1
red_level = N-1
blue_level = N-1

while True:
    if red_level >= 1:
        blue[red_level] += X * red[red_level]
        blue_level = red_level
        red[red_level-1], red[red_level] = red[red_level], red[red_level-1]
        red_level -= 1
    
    if blue_level >= 1:
        red[blue_level-1] += blue[blue_level]
        blue[blue_level-1], blue[blue_level] = blue[blue_level] * Y, blue[blue_level-1]
        blue_level -= 1
        
    if red_level == 0 and blue_level == 0:
        break

print(blue[0])
