use proconio::{fastout, input};
use std::collections::HashMap;


#[fastout]
fn main() {
    input! {
        w: String,
    }

    let count = w.chars().fold(HashMap::new(), |mut acc, c| {
        *acc.entry(c).or_insert(0) += 1;
        acc
    });

    let b = count.values().all(|&v| v % 2 == 0);
    println!("{}", if b { "Yes" } else { "No" });
}   
