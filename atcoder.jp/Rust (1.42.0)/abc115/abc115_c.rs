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

    let ans = h
        .windows(k)
        .fold(std::i64::MAX, |acc, x| min(acc, x[k - 1] - x[0]));

    println!("{}", ans);
}
