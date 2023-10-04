include atcoder/header
proc `//`(a, b: int): int = a div b

var
    N, K, X = nextInt()
    A = newSeqWith(N, nextInt()).sorted.reversed

for i in 0..<N:
    let k = (A[i] // X).min(K)
    K -= k
    A[i] -= k * X
    if K == 0:
        break

A.sort
A.reverse
A = A[K.min(N)..<N]

echo A.sum
