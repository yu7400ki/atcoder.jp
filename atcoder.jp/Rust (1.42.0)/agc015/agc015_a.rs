use proconio::{fastout, input};
use std::cmp::max;

#[fastout]
fn main() {
    input! {
        n: i64,
        a: i64,
        b: i64,
    }

    let mi = a * (n - 1) + b;
    let ma = a + b * (n - 1);

    println!("{}", max(0, ma - mi + 1));
}
