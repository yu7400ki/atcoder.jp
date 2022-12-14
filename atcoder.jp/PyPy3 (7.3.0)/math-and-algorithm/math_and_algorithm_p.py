from functools import lru_cache

def main():
    n = int(input())
    A = list(map(int,input().split()))

    @lru_cache(maxsize=1000)
    def gcd(a,b):
        R = a % b
        if R == 0:
            return b
        else:
            return gcd(b,R)

    a = A[0]
    for i in range(1,n):
        a = gcd(a, A[i])

    return a

if __name__ == '__main__':
    print(main())