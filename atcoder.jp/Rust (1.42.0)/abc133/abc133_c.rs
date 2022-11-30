use proconio::{fastout, input};

const MOD: i64 = 2019;

#[fastout]
fn main() {
    input! {
        l: i64,
        r: i64,
    }

    let mut ans = MOD;

    if r - l + 1>= MOD {
        ans = 0;
    } else {
        for i in l..=r {
            for j in i + 1..=r {
                ans = ans.min((i * j) % MOD);
            }
        }
    }

    println!("{}", ans);
}   
