N = int(input())
S = list(input())
left = S[:N]
right = S[N:]
Q = int(input())

for _ in range(Q):
	T, A, B = map(int,input().split())
	if T == 2:
		left, right = right, left
	else:
		if A > N:
			A -= N
			B -= N
			right[A-1], right[B-1] = right[B-1], right[A-1]
		else:
			if B > N:
				B -= N
				left[A-1], right[B-1] = right[B-1], left[A-1]
			else:
				left[A-1], left[B-1] = left[B-1], left[A-1]

print(''.join(left) + ''.join(right))