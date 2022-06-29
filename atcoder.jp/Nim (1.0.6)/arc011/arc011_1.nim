import strutils
import sequtils
import strformat

var m, n, N: int
(m, n, N) = stdin.readLine.split.map(parseInt)
var ans: int = 0
var c: int = 0

while true:
    ans += N
    c += N
    if c >= m:
        N = c div m * n
        c = c mod m
    else:
        break

echo ans