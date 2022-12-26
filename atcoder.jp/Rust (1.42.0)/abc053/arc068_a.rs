use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        mut x: u64,
    }

    let mut ans = x / 11 * 2;
    x = x % 11;

    if x > 6 {
        ans += 2;
    } else if x > 0 {
        ans += 1;
    }

    println!("{}", ans);
}
