use proconio::{fastout, input};
use std::cmp::{max, min};

const MOD: usize = 1_000_000_007;

fn permutation(n: usize, k: usize, m: usize) -> usize {
    let mut ans = 1;
    for i in 0..k {
        ans = ans * (n - i) % m;
    }
    ans
}

#[fastout]
fn main() {
    input! {
        n: usize,
        m: usize,
    }

    if max(n, m) - min(n, m) > 1 {
        println!("0");
        return;
    }

    let ans = if n == m {
        permutation(n, n, MOD) % MOD * permutation(m, m, MOD) % MOD * 2 % MOD
    } else {
        permutation(n, n, MOD) % MOD * permutation(m, m, MOD) % MOD
    };

    println!("{}", ans);
}
