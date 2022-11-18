use proconio::{fastout, input};
use std::cmp::min;

#[fastout]
fn main() {
    input! {
        n: usize,
        b: [i64; n-1],
    }

    let mut a = vec![0; n];
    a[0] = b[0];

    for (i, v) in b.iter().enumerate() {
        a[i] = min(a[i], *v);
        a[i+1] = *v;
    }

    println!("{}", a.iter().sum::<i64>());
}   
