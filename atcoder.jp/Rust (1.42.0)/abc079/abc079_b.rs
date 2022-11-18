use proconio::{fastout, input};

fn l(n: i64, a: i64, b: i64) -> i64 {
    if n == 0 {
        a
    } else {
        l(n - 1, b, a + b)
    }
}

#[fastout]
fn main() {
    input! {
        n: i64,
    }

    println!("{}", l(n, 2, 1));
}   
