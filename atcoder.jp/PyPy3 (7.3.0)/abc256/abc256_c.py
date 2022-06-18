h1,h2,h3,w1,w2,w3 = map(int,input().split())

ceil = [[1] * 3 for _ in range(3)]

cnt = 0
for i in range(1,30):
	for j in range(1,30):
		if i + j < h1: H1 = h1 - i - j
		else: break
		for k in range(1,30):
			if i + k < w1: W1 = w1 - i - k
			else: break
			for l in range(1,30):
				if k + l < h2: H2 = h2 - k - l
				else: break
				if j + l < w2: W2 = w2 - j - l
				else: break
				if H1 + H2 < w3 and W1 + W2 < h3:
					if w3 - H1 - H2 == h3 - W1 - W2: cnt += 1

print(cnt)
