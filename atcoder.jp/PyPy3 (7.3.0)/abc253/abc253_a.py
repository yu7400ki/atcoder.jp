from statistics import median

a,b,c = map(int,input().split())
print('Yes' if median([a,b,c]) == b else 'No')