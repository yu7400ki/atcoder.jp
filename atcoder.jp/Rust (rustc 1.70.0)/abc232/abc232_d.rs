use proconio::{input, fastout, marker::Chars};
use std::collections::VecDeque;

#[fastout]
fn main() {
    input! {
        h: usize,
        w: usize,
        s: [Chars; h],
    }

    let mut depth = vec![vec![0; w]; h];
    let mut q = VecDeque::new();
    depth[0][0] = 1;
    q.push_back((0, 0));

    while let Some((x, y)) = q.pop_front() {
        let d = depth[y][x];
        for &(dx, dy) in &[(1, 0), (0, 1)] {
            let nx = x + dx;
            let ny = y + dy;
            if nx >= w || ny >= h {
                continue;
            }
            if s[ny][nx] == '#' {
                continue;
            }
            if depth[ny][nx] != 0 {
                continue;
            }
            depth[ny][nx] = d + 1;
            q.push_back((nx, ny));
        }
    }

    let ans = depth.iter().flatten().max().unwrap();
    println!("{}", ans);
}
