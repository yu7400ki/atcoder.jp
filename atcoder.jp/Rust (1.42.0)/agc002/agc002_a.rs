use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        a: i64,
        b: i64,
    }

    if a <= 0 && 0 <= b {
        println!("Zero");
    } else if a > 0 {
        println!("Positive");
    } else {
        let n = b - a + 1;
        if n % 2 == 0 {
            println!("Positive");
        } else {
            println!("Negative");
        }
    }
}   
