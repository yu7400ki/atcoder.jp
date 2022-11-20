use proconio::{fastout, input};
use std::cmp::min;

#[fastout]
fn main() {
    input! {
        a: i64,
        b: i64,
        c: i64,
        x: i64,
        y: i64,
    }

    let mut ans = 0;

    if a + b > c * 2 {
        if x > y {
            ans += c * 2 * y;
            ans += min(a, c * 2) * (x - y);
        } else {
            ans += c * 2 * x;
            ans += min(b, c * 2) * (y - x);
        }
    } else {
        ans += a * x;
        ans += b * y;
    }

    println!("{}", ans);
}
