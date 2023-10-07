use proconio::{fastout, input};
use std::collections::HashMap;

#[fastout]
fn main() {
    input! {
        n: usize,
    }

    let mut slimes = HashMap::new();
    for _ in 0..n {
        input! {
            s: u64,
            c: u64,
        }
        let i = s.trailing_zeros();
        *slimes.entry(s >> i).or_insert(0) += c << i;
    }

    let ans = slimes.values().map(|&x| x.count_ones()).sum::<u32>();
    println!("{}", ans);
}
