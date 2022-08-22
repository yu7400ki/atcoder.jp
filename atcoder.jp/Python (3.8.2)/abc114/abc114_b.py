S = input()

mi = float('inf')
for i in range(len(S)-2):
    mi = min(mi, abs(int(S[i:i+3]) - 753))

print(mi)