use proconio::{fastout, input};
use std::cmp::min;

#[fastout]
fn main() {
    input! {
        n: u64,
        a: u64,
        b: u64,
    }

    let dist = b - a;
    let ans = if dist % 2 == 0 {
        dist / 2
    } else {
        min(a - 1, n - b) + 1 + (b - a - 1) / 2
    };

    println!("{}", ans);
}
