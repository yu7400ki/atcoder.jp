S = list(map(int, input().split()))

def is_valid(n):
    if not (100 <= n <= 675):
        return False
    if n % 25 != 0:
        return False
    return True

if sorted(S) != S:
    print('No')
    exit()

if all(is_valid(n) for n in S):
    print('Yes')
else:
    print('No')
