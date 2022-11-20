use proconio::{fastout, input};
use std::cmp::max;

fn accumulate(a: &Vec<i64>) -> Vec<i64> {
    let mut acc = vec![0; a.len() + 1];
    for i in 0..a.len() {
        acc[i + 1] = acc[i] + a[i];
    }
    acc
}

#[fastout]
fn main() {
    input! {
        n: usize,
        a1: [i64; n],
        a2: [i64; n],
    }

    let accum_a1 = accumulate(&a1);
    let accum_a2 = accumulate(&a2);

    let mut ans = 0;
    for i in 0..n {
        ans = max(ans, (accum_a1[i + 1] - accum_a1[0]) + (accum_a2[n] - accum_a2[i]));
    }

    println!("{}", ans);
}
