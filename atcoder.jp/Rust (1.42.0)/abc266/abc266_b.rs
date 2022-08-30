use proconio::{fastout, input};

const MOD: i64 = 998244353;

#[fastout]
fn main() {
    input! {
        n: i64,
    }

    let mut ans: i64 = n % MOD;
    if ans < 0 {
        ans += MOD;
    }

    println!("{}", ans);
}   
