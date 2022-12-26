use proconio::marker::{Chars, Usize1};
use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        q: usize,
        s: Chars,
    }
    
    let flag = s
        .windows(2)
        .map(|w| w == ['A', 'C'])
        .collect::<Vec<_>>();

    let mut sum = vec![0; n];
    for i in 1..n {
        sum[i] = sum[i - 1] + flag[i - 1] as usize;
    }

    for _ in 0..q {
        input! {
            l: Usize1,
            r: Usize1,
        }
        println!("{}", sum[r] - sum[l]);
    }
}
