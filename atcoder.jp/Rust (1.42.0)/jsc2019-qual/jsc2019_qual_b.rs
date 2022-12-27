use proconio::{fastout, input};

const MOD: i64 = 1_000_000_007;

fn inversion_num(a: &[i64]) -> i64 {
    let mut ans = 0;
    let n = a.len();
    for i in 0..n {
        for j in i + 1..n {
            if a[i] > a[j] {
                ans += 1;
                ans %= MOD;
            }
        }
    }
    ans
}

fn combination(n: i64, r: i64) -> i64 {
    let mut res = 1;
    for i in 0..r {
        res *= n - i;
        res /= i + 1;
        res %= MOD;
    }
    res
}

#[fastout]
fn main() {
    input! {
        n: usize,
        k: i64,
        a: [i64; n],
    }

    let mut ans = inversion_num(&a) * k;
    ans %= MOD;

    let mut cnt = 0;
    for i in 0..n {
        for j in 0..n {
            if a[i] < a[j] {
                cnt += 1;
                cnt %= MOD;
            }
        }
    }

    ans += cnt * combination(k, 2);
    ans %= MOD;

    println!("{}", ans);
}
