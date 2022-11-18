use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        a: i64,
        b: i64,
    }

    for i in 1..10000 {
        let i = i * 100;
        if (i / 100 * 8) / 100 == a && (i / 100 * 10) / 100 == b {
            println!("{}", i / 100);
            return;
        }
    }

    println!("-1");
}   
