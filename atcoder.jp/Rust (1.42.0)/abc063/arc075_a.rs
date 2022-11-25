use proconio::{fastout, input};

const LIMIT: usize = 100 * 100 + 1;

#[fastout]
fn main() {
    input! {
        n: usize,
        s: [i64; n],
    }

    let mut dp = vec![vec![false; LIMIT]; n + 1];
    dp[0][0] = true;

    for i in 0..n {
        for j in 0..LIMIT {
            dp[i + 1][j] |= dp[i][j];
            if j as i64 + s[i] < LIMIT as i64 {
                dp[i + 1][j + s[i] as usize] |= dp[i][j];
            }
        }
    }

    let ans = dp[n]
        .iter()
        .enumerate()
        .filter(|(i, &x)| x && i % 10 != 0)
        .map(|(i, _)| i)
        .max()
        .unwrap_or(0);

    println!("{}", ans);
}
