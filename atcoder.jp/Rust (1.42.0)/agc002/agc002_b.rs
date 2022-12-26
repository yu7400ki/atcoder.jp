use std::vec;

use proconio::{fastout, input};
use proconio::marker::Usize1;

#[fastout]
fn main() {
    input! {
        n: usize,
        m: usize,
    }

    let mut b = vec![false; n];
    let mut cnt = vec![1; n];
    b[0] = true;

    for _ in 0..m {
        input! {
            x: Usize1,
            y: Usize1,
        }

        b[y] |= b[x];
        cnt[x] -= 1;
        cnt[y] += 1;

        if cnt[x] == 0 {
            b[x] = false;
        }
    }

    let ans = b.iter().filter(|&&x| x).count();

    println!("{}", ans);
}
