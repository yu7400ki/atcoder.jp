use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
    }

    let mut dp = vec![vec![-1_isize; 3]; n + 1];
    dp[0][0] = 0;

    for i in 0..n {
        input! {
            x: usize,
            y: isize,
        }
        for j in 0..2 {
            if dp[i][j] == -1 {
                continue;
            }
            match x {
                0 => {
                    let idx = if j > 0 { j - 1 } else { j };
                    dp[i + 1][idx] = dp[i + 1][idx].max(dp[i][j] + y);
                    dp[i + 1][j] = dp[i + 1][j].max(dp[i][j])
                }
                1 => {
                    dp[i + 1][j + 1] = dp[i + 1][j + 1].max(dp[i][j] + y);
                    dp[i + 1][j] = dp[i + 1][j].max(dp[i][j]);
                }
                _ => unreachable!(),
            }
        }
    }

    let ans = dp[n][0].max(dp[n][1]);
    println!("{}", ans);
}
