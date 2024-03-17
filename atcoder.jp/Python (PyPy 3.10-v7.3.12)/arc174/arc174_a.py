N, C = map(int, input().split())
A = list(map(int, input().split()))

def max_subarray(lst):
    max_sum = -1
    max_start = 0
    max_end = 0
    current_sum = 0
    current_start = 0
    for i, a in enumerate(lst):
        current_sum += a
        if current_sum > max_sum:
            max_sum = current_sum
            max_start = current_start
            max_end = i
        if current_sum < 0:
            current_sum = 0
            current_start = i + 1
    return max_sum, max_start, max_end

if C > 0:
    _, l, r = max_subarray(A)
else:
    _, l, r = max_subarray(-a for a in A)

print(max(sum(A[:l]) + sum(A[l : r + 1]) * C + sum(A[r + 1 :]), sum(A)))
