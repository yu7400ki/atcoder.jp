use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        a: i64,
        b: i64,
        c: i64,
    }

    let d = c - a - b;

    if d > 0 && 4 * a * b < d * d {
        println!("Yes");
    } else {
        println!("No");
    }
}
