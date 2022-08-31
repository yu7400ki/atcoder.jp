use proconio::{fastout, input};
use std::cmp::{min, max};

#[fastout]
fn main() {
    input! {
        n: usize,
        a: [usize; n],
    }

    let mut cnt = 0i64;
    let mut ans = 0i64;

    for j in 0..n {
        if a[j] == j+1 {
            ans += cnt;
            cnt += 1;
        } else {
            let i = a[j] - 1;
            if min(a[i], a[j]) == i+1 && max(a[i], a[j]) == j+1 {
                ans += 1;
            }
        }
    }

    println!("{}", ans);
}   
