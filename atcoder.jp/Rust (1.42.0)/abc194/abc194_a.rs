use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        a: usize,
        b: usize,
    }

    let c = a + b;
    let ans = if c >= 15 && b >= 8 {
        1
    } else if c >= 10 && b >= 3 {
        2
    } else if c >= 3 {
        3
    } else {
        4
    };

    println!("{}", ans);
}
