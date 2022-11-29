use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        mut n: i64,
        mut m: i64,
    }

    let mut ans = 0;
    if m >= n * 2 {
        ans += n;
        m -= n * 2;
    } else {
        ans += m / 2;
        m = 0;
    }

    ans += m / 4;

    println!("{}", ans);
}
