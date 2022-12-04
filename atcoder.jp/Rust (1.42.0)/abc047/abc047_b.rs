use proconio::{fastout, input};
use std::cmp::{max, min};

#[fastout]
fn main() {
    input! {
        w: i64,
        h: i64,
        n: i64,
    }

    let mut t: i64 = 0;
    let mut r: i64 = w;
    let mut b: i64 = h;
    let mut l: i64 = 0;

    for _ in 0..n {
        input! {
            x: i64,
            y: i64,
            a: i64,
        }

        match a {
            1 => {
                l = max(l, x);
            }
            2 => {
                r = min(r, x);
            }
            3 => {
                t = max(t, y);
            }
            4 => {
                b = min(b, y);
            }
            _ => unreachable!(),
        }
    }

    let width = max(r - l, 0);
    let height = max(b - t, 0);
    let ans = width * height;

    println!("{}", ans);
}
