use itertools::Itertools;
use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        m: usize,
        mut x: [i64; m],
    }

    if m <= n {
        println!("0");
        return;
    }

    x.sort();
    let d = x.windows(2).map(|w| w[1] - w[0]).sorted().collect::<Vec<_>>();
    let ans = d[..m - n].iter().sum::<i64>();

    println!("{}", ans);
}
