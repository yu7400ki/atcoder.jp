include atcoder/header

proc `//`(a, b: int): int = a div b
proc rev(a, b: int): int = cmp(b, a)

var
    N, K, X = nextInt()
    A = newSeqWith(N, nextInt()).sorted rev

for i in 0..<N:
    let k = (A[i] // X).min(K)
    K -= k
    A[i] -= k * X
    if K == 0:
        break

A.sort rev
A = A[K.min(N)..<N]

echo A.sum
