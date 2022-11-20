use proconio::{fastout, input};
use std::cmp::max;

#[fastout]
fn main() {
    input! {
        x: u32,
    }

    let mut ans = 0;

    for i in 0..1000u32 {
        for j in 2..1000u32 {
            let tmp = i.pow(j);
            if tmp <= x {
                ans = max(ans, tmp);
            } else {
                break;
            }
        }
    }

    println!("{}", ans);
}
