use proconio::{input, fastout};
use std::collections::VecDeque;

#[fastout]
fn main() {
    input! {
        n: usize,
        q: usize,
    }

    let mut d = VecDeque::with_capacity(n);
    for i in 0..n {
        d.push_back((i as i32 + 1, 0));
    }

    for _ in 0..q {
        input! {
            t: usize,
        }

        match t {
            1 => {
                input! {
                    c: char,
                }
                let dx = match c {
                    'L' => -1,
                    'R' => 1,
                    _ => 0,
                };
                let dy = match c {
                    'U' => 1,
                    'D' => -1,
                    _ => 0,
                };
                let head = d[0];
                d.push_front((head.0 + dx, head.1 + dy));
            },
            2 => {
                input! {
                    p: usize,
                }
                println!("{} {}", d[p - 1].0, d[p - 1].1);
            },
            _ => unreachable!(),
        }
    }
}
