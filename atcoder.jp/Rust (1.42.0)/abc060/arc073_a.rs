use proconio::{fastout, input};
use std::cmp::max;

#[fastout]
fn main() {
    input! {
        n: usize,
        l: i64,
        t: [i64; n],
    }

    let mut ans = l;
    
    for i in 1..n {
        let overlap = max(0, t[i-1] + l - t[i]);
        ans += l - overlap;
    }

    println!("{}", ans);
}
