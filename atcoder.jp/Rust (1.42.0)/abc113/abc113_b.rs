use proconio::{fastout, input};
use std::f64;

#[fastout]
fn main() {
    let mut diff: f64 = f64::MAX;
    let mut ans: usize = 0;
    input! {
        n: usize,
        t: f64,
        a: f64,
        h: [f64; n],
    }
    for i in 0..n {
        let ave:f64 = t - h[i] * 0.006 as f64;
        if (ave - a).abs() < diff{
            diff = (ave - a).abs();
            ans = i + 1;
        }
    }
    println!("{}", ans);
}