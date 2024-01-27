use itertools::Itertools;
use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {
        s: Chars,
    }

    let cnt = s.iter().fold(vec![0u8; 26], |mut acc, c| {
        acc[(*c as u8 - b'a') as usize] += 1;
        acc
    });
    let ans = 25 - cnt.iter().rev().position_max().unwrap() as u8 + b'a';
    println!("{}", ans as char);
}
