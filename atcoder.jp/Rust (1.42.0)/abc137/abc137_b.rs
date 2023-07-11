use itertools::Itertools;
use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        k: isize,
        x: isize,
    }

    let ans = ((x - k + 1)..(x + k)).join(" ");

    println!("{}", ans);
}
