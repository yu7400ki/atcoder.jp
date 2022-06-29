import strformat, strutils, sequtils, math, algorithm, tables, sets, lists, intsets, critbits, future

var
    H, W: int
(H, W) = stdin.readLine.split.map(parseInt)
let
    grid = (0..<H).mapIt(stdin.readLine)

var flag: bool
for i in 0..<H:
    for j in 0..<W:
        flag = false
        if grid[i][j] == '#':
            if i > 0:
                if grid[i - 1][j] == '#':
                    flag = true
            if j > 0:
                if grid[i][j - 1] == '#':
                    flag = true
            if i < H - 1:
                if grid[i + 1][j] == '#':
                    flag = true
            if j < W - 1:
                if grid[i][j + 1] == '#':
                    flag = true
            if not flag:
                echo "No"
                quit 0


echo "Yes"