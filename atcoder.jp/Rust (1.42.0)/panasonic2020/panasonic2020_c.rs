use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        a: u64,
        b: u64,
        c: u64,
    }

    let d = c - a - b;

    if d > 0 && 4 * a * b < d * d {
        println!("Yes");
    } else {
        println!("No");
    }
}
