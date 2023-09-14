use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
    }

    let mut d = vec![vec![0; n]; n];
    for i in 1..n {
        input! {
            di: [usize; n - i],
        }
        for j in 0..n - i {
            d[i - 1][i + j] = di[j];
            d[i + j][i - 1] = di[j];
        }
    }

    let mut dp = vec![0; 1 << n];
    for b in 0_usize..(1 << n) - 1 {
        let l = b.trailing_ones() as usize;
        for i in l + 1..n {
            if (b >> i & 1) == 0 {
                let nb = (b | 1 << i | 1 << l);
                dp[nb] = dp[nb].max(dp[b] + d[l][i]);
            }
        }
    }

    let ans = dp.last().unwrap();
    println!("{}", ans);
}
