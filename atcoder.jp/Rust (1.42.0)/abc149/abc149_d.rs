use proconio::{fastout, input};

macro_rules! max {
    ($x:expr) => ( $x );
    ($x:expr, $($xs:expr),+) => {
        std::cmp::max($x, max!( $($xs),+ ))
    };
}

#[fastout]
fn main() {
    input! {
        (n, k): (usize, usize),
        rsp: [usize; 3],
        t: String,
    }

    let t = t
        .chars()
        .map(|c| match c {
            'r' => 0,
            's' => 1,
            'p' => 2,
            _ => unreachable!(),
        })
        .collect::<Vec<_>>();

    let mut ans = 0;

    for i in 0..k {
        let iter = (i..n).step_by(k).collect::<Vec<_>>();
        let mut dp = vec![vec![0; 3]; iter.len()];
        match t[i] {
            0 => dp[0][2] = rsp[2],
            1 => dp[0][0] = rsp[0],
            2 => dp[0][1] = rsp[1],
            _ => unreachable!(),
        }
        for j in 1..iter.len() {
            let i = iter[j];
            for k in 0..3 {
                for l in 0..3 {
                    if k == l {
                        continue;
                    }
                    let score = if (t[i] - k as i32 + 3) % 3 == 1 {
                        rsp[k]
                    } else {
                        0
                    };
                    dp[j][k] = max!(dp[j][k], dp[j - 1][l] + score);
                }
            }
        }
        ans += dp.last().unwrap().iter().max().unwrap();
    }

    println!("{}", ans);
}
