include atcoder/header

let
    N = nextInt()
    A = newSeqWith(N, nextInt())
    Q = nextInt()

var counter = newSeqWith(100001, 0)
for a in A:
    counter[a] += 1
var ans = A.sum

for _ in 0..<Q:
    let B, C = nextInt()
    ans -= B * counter[B]
    ans += C * counter[B]
    counter[C] += counter[B]
    counter[B] = 0
    echo ans
