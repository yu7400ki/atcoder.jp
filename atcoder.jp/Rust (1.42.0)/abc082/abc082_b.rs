use itertools::Itertools;
use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        s: String,
        t: String,
    }

    let s = s.chars().sorted().collect::<String>();
    let t = t.chars().sorted().rev().collect::<String>();

    if s < t {
        println!("Yes");
    } else {
        println!("No");
    }
}
