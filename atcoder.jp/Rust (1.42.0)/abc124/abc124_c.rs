use proconio::{fastout, input};
use std::cmp::min;

#[fastout]
fn main() {
    input! {
        s: String,
    }

    let mut odd = 0;
    let mut even = 0;

    for (i, c) in s.chars().enumerate() {
        if c == '0' {
            if i % 2 == 0 {
                even += 1;
            } else {
                odd += 1;
            }
        } else {
            if i % 2 == 0 {
                odd += 1;
            } else {
                even += 1;
            }
        }
    }

    println!("{}", min(odd, even));
}   
