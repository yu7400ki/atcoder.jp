use proconio::{input, fastout};

#[fastout]
fn main() {
    input! {
        n: usize,
        x: usize,
        y: usize,
        ab: [(usize, usize); n],
    }

    let inf = 1_000_000_000;
    let mut dp = vec![vec![vec![inf; y+1]; x+1]; n+1];
    dp[0][0][0] = 0;

    for i in 0..n {
        for j in 0..=x {
            for k in 0..=y {
                if dp[i][j][k] != inf {
                    dp[i+1][j][k] = dp[i+1][j][k].min(dp[i][j][k]);
                    let l = (j + ab[i].0).min(x);
                    let m = (k + ab[i].1).min(y);
                    dp[i+1][l][m] = dp[i+1][l][m].min(dp[i][j][k] + 1);
                }
            }
        }
    }

    let mut ans = inf;
    for i in 1..=n {
        if dp[i][x][y] != inf {
            ans = ans.min(dp[i][x][y])
        }
    }
    if ans == inf {
        ans = -1;
    }

    println!("{}", ans);
}
