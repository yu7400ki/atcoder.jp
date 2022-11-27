use proconio::{fastout, input};
use std::cmp::{max, min};

#[fastout]
fn main() {
    input! {
        n: i64,
        m: i64,
    }

    let (n, m) = (min(n, m), max(n, m));

    if n == 1 {
        if m == 1 {
            println!("1");
        } else {
            println!("{}", m - 2);
        }
    } else {
        println!("{}", (n - 2) * (m - 2));
    }
}   
