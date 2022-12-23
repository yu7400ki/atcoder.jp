use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: i64,
        m: i64,
    }

    let time = 2i64.pow(m as u32);

    let mut ans = 0;
    ans += m * 1900 * time;
    ans += (n - m) * 100 * time;

    println!("{}", ans);
}
