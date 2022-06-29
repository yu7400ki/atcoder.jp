import strutils
import sequtils
import strformat
import future

var N, K: int
(N, K) = stdin.readLine.split.map(parseInt)
var 
    A = stdin.readLine.split.map(parseInt)
    B = stdin.readLine.split.map(parseInt)
    dp:seq[bool] = repeat(false, N)
    ep:seq[bool] = repeat(false, N)

dp[0] = true
ep[0] = true

for i in 1..N-1:
    if dp[i-1]:
        if abs(A[i-1] - A[i]) <= K:
            dp[i] = true
        if abs(A[i-1] - B[i]) <= K:
            ep[i] = true
    if ep[i-1]:
        if abs(B[i-1] - A[i]) <= K:
            dp[i] = true
        if abs(B[i-1] - B[i]) <= K:
            ep[i] = true

if dp[N-1] or ep[N-1]:
    echo "Yes"
else:
    echo "No"