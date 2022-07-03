import strformat, strutils, sequtils, math, algorithm, tables, sets, lists, intsets, critbits, future

var
    N, T, A, B:int
    X, ans:int64
(N, X) = stdin.readLine.split.map(parseInt)

for i in 1..min(N, X):
    (A, B) = stdin.readLine.split.map(parseInt)
    T += A + B
    if i == 1:
        ans = T + (X - i) * B
    else:
        ans = min(ans, T + (X - i) * B)

echo ans