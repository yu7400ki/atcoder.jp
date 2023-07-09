use proconio::{fastout, input, marker::Usize1};

#[fastout]
fn main() {
    input! {
        n: usize,
        m: usize,
        p: [Usize1; n - 1],
    }
    let mut dp = vec![-1; n];
    for _ in 0..m {
        input! {
            x: Usize1,
            y: isize,
        }
        dp[x] = dp[x].max(y);
    }
    for i in 1..n {
        dp[i] = dp[i].max(dp[p[i - 1]] - 1)
    }
    let ans = dp.iter().fold(0, |p, &c| p + (c >= 0) as usize);
    println!("{}", ans);
}
