use proconio::{fastout, input, marker::Chars};
use std::collections::VecDeque;

#[fastout]
fn main() {
    input! {
        h: usize,
        _w: usize,
        mut a: [Chars; h],
    }

    pre(&mut a);
    let (start, end) = start_end(&a);
    let depth = solve(start, end, &a);
    let ans = if depth[end.0][end.1] == 0 {
        -1
    } else {
        depth[end.0][end.1]
    };
    println!("{}", ans);
}

fn pre(a: &mut Vec<Vec<char>>) {
    let h = a.len();
    let w = a[0].len();
    for i in 0..h {
        for j in 0..w {
            let c = a[i][j];
            match c {
                'v' | '^' | '<' | '>' => {
                    let (dx, dy) = match c {
                        'v' => (0, 1),
                        '^' => (0, -1),
                        '<' => (-1, 0),
                        '>' => (1, 0),
                        _ => unreachable!(),
                    };
                    let (mut x, mut y) = (j as i32, i as i32);
                    x += dx;
                    y += dy;
                    while 0 <= x && x < w as i32 && 0 <= y && y < h as i32 {
                        if a[y as usize][x as usize] != '.' && a[y as usize][x as usize] != '!' {
                            break;
                        }
                        a[y as usize][x as usize] = '!';
                        x += dx;
                        y += dy;
                    }
                }
                _ => {}
            }
        }
    }
}

fn start_end(a: &Vec<Vec<char>>) -> ((usize, usize), (usize, usize)) {
    let h = a.len();
    let w = a[0].len();
    let mut start = (0, 0);
    let mut end = (0, 0);
    for i in 0..h {
        for j in 0..w {
            if a[i][j] == 'S' {
                start = (i, j);
            }
            if a[i][j] == 'G' {
                end = (i, j);
            }
        }
    }
    (start, end)
}

fn solve(start: (usize, usize), end: (usize, usize), a: &Vec<Vec<char>>) -> Vec<Vec<isize>> {
    let h = a.len();
    let w = a[0].len();
    let mut depth = vec![vec![-1; w]; h];
    depth[start.0][start.1] = 0;
    let mut q = VecDeque::new();
    q.push_back(start);
    while let Some((y, x)) = q.pop_front() {
        for (dx, dy) in [(0, 1), (0, -1), (-1, 0), (1, 0)].iter() {
            let (nx, ny) = (x as i32 + dx, y as i32 + dy);
            if 0 <= nx && nx < w as i32 && 0 <= ny && ny < h as i32 {
                if (ny as usize, nx as usize) == end {
                    depth[ny as usize][nx as usize] = depth[y][x] + 1;
                    return depth;
                }
                if a[ny as usize][nx as usize] == '.' && depth[ny as usize][nx as usize] == -1 {
                    depth[ny as usize][nx as usize] = depth[y][x] + 1;
                    q.push_back((ny as usize, nx as usize));
                }
            }
        }
    }
    depth
}
