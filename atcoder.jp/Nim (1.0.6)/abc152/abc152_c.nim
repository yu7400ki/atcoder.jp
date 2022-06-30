import strformat, strutils, sequtils, math, algorithm, tables, sets, lists, intsets, critbits, future

let
    _ = stdin.readLine.parseInt
    P = stdin.readLine.split.map(parseInt)

var
    ans: int = 0
    mi: int = P[0]

for i in 0..<len(P):
    mi = min(mi, P[i])
    if P[i] <= mi:
        ans += 1

echo ans