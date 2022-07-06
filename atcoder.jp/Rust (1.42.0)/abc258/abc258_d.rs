use proconio::{input, fastout};
use std::cmp::min;
use std::usize;

#[fastout]
fn main() {
    let mut now = 0;
    let mut ans = usize::MAX;
    input! {
        n: usize,
        x: usize,
        t: [(usize, usize); n],
    };
    for i in 0..(min(n,x)) {
        let (a, b) = t[i];
        now += a + b;
        ans = min(ans, now + (x - i - 1) * b);
    }
    println!("{}", ans);
}
