def solve():
    from collections import Counter

    N = int(input())
    A = list(map(int, input().split()))

    count = Counter(A)
    for i in sorted(list(set(A)), reverse=True):
        print(count[i])
    for _ in range(N - len(count)):
        print(0)

if __name__ == "__main__":
    solve()
