use proconio::{fastout, input};



#[fastout]
fn main() {
    input! {
        a: i64,
        b: i64,
        _c: i64,
        k: i64,
    }

    println!("{}", (a - b) * if k % 2 == 0 { 1 } else { -1 });
}   
