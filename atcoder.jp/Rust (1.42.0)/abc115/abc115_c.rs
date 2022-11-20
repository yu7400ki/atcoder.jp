use proconio::{fastout, input};
use std::cmp::min;

#[fastout]
fn main() {
    input! {
        n: usize,
        k: usize,
        mut h: [i64; n],
    }

    h.sort();
    let mut ans = 1 << 60;

    for i in 0..n - k + 1 {
        let hmin = h[i];
        let hmax = h[i + k - 1];
        ans = min(ans, hmax - hmin);
    }

    println!("{}", ans);
}
