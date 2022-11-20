use proconio::{fastout, input};
use std::cmp::max;

#[fastout]
fn main() {
    input! {
        n: u64,
    }

    let len = n.to_string().len() as u64;

    let mut ans = n
        .to_string()
        .chars()
        .map(|c| c.to_digit(10).unwrap() as u64)
        .sum::<u64>();

    ans = max(
        ans,
        n.to_string().chars().nth(0).unwrap().to_digit(10).unwrap() as u64 + 9 * (len - 1) - 1,
    );

    println!("{}", ans);
}
