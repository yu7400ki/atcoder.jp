use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        a: i64,
        b: i64,
        c: i64,
    }

    for i in 1..=b {
        if a * i % b == c {
            println!("YES");
            return;
        }
    }

    println!("NO");
}
