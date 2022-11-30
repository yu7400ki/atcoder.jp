use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        w: i64,
        h: i64,
        x: i64,
        y: i64,
    }

    let area = w * h;
    let a = if x * 2 == w && y * 2 == h { 1 } else { 0 };

    println!("{} {}", area as f64 / 2.0, a);
}
