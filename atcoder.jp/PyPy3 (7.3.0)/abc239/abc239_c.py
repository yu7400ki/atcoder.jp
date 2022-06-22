x1, y1, x2, y2 = map(int, input().split())

one = set([(x1+2,y1+1), (x1+1,y1+2), (x1+2,y1-1), (x1+1,y1-2), (x1-1,y1+2), (x1-2,y1+1), (x1-2,y1-1), (x1-1,y1-2)])
two = set([(x2+2,y2+1), (x2+1,y2+2), (x2+2,y2-1), (x2+1,y2-2), (x2-1,y2+2), (x2-2,y2+1), (x2-2,y2-1), (x2-1,y2-2)])

print('Yes' if one & two else 'No')