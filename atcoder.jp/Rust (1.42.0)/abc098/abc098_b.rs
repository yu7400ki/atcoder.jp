use proconio::{fastout, input};
use std::collections::HashSet;
use std::cmp::max;

#[fastout]
fn main() {
    input! {
        n: usize,
        s: String,
    }

    let mut ans = 0;

    for i in 1..n {
        let left = s[..i].chars().collect::<HashSet<_>>();
        let right = &s[i..].chars().collect::<HashSet<_>>();
        
        let res = left.intersection(right).count();
        ans = max(ans, res);
    }

    println!("{}", ans);
}
