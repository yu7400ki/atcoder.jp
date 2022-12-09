use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        mut x: i64,
        y: i64,
    }

    let mut ans = 0;

    if y < x {
        ans += 1;
        x *= -1;
    }

    ans += (y.abs() - x.abs()).abs();

    if y < x {
        ans += 1;
    }

    println!("{}", ans);
}
