use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        x: i64,
    }

    println!("{}", if x % 615 == 0 { "1" } else { "0" });
}
