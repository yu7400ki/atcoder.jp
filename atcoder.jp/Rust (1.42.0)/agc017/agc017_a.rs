use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        p: usize,
        a: [usize; n],
    }

    let ma = a.iter().max().unwrap();
    let limit = ma * n + 1;

    let mut dp = vec![vec![0; limit]; n + 1];
    dp[0][0] = 1;

    for i in 0..n {
        for j in 0..limit {
            dp[i + 1][j] += dp[i][j];
            if j + a[i] < limit {
                dp[i + 1][j + a[i]] += dp[i][j];
            }
        }
    }

    let ans = dp[n]
        .iter()
        .enumerate()
        .filter(|&(i, &_)| i % 2 == p)
        .map(|(_, &v)| v)
        .sum::<usize>();

    println!("{}", ans);
}
