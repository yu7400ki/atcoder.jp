use proconio::{input, fastout};
use std::collections::HashSet;

#[fastout]
fn main() {
    input! {
        n: i32,
        mut d: [i32; n],
    };

    let d: HashSet<i32> = d.into_iter().collect();
    println!("{}", d.len());
}
