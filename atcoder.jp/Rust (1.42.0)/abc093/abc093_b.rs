use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        a: i64,
        b: i64,
        k: i64,
    }

    if a + k > b - k {
        for i in a..=b {
            println!("{}", i);
        }
    } else {
        for i in a..a + k {
            println!("{}", i);
        }
        for i in b - k + 1..=b {
            println!("{}", i);
        }
    }
}   
