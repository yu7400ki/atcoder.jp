use proconio::{input, fastout};
use std::cmp::min;
use std::usize;

#[fastout]
fn main() {
    let mut ans= usize::MAX;
    input! {
        n: usize,
        x: [usize; n],
    };
    for i in 1..=100 {
        let mut sum = 0;
        for j in x.iter() {
            sum += (j - i).pow(2);
        }
        ans = min(ans, sum);
    }
    println!("{}", ans);
}
