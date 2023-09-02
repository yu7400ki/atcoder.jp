use proconio::{fastout, input};

macro_rules! chmax {
    ($base:expr, $($cmps:expr),+ $(,)*) => {{
        let cmp_max = max!($($cmps),+);
        if $base < cmp_max {
            $base = cmp_max;
            true
        } else {
            false
        }
    }};
}

macro_rules! max {
    ($a:expr $(,)*) => {{
        $a
    }};
    ($a:expr, $b:expr $(,)*) => {{
        std::cmp::max($a, $b)
    }};
    ($a:expr, $($rest:expr),+ $(,)*) => {{
        std::cmp::max($a, max!($($rest),+))
    }};
}

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
                    chmax!(dp[i + 1][idx], dp[i][j] + y);
                    chmax!(dp[i + 1][j], dp[i][j]);
                }
                1 => {
                    chmax!(dp[i + 1][j + 1], dp[i][j] + y);
                    chmax!(dp[i + 1][j], dp[i][j]);
                }
                _ => unreachable!(),
            }
        }
    }

    let ans = dp[n][0].max(dp[n][1]);
    println!("{}", ans);
}
