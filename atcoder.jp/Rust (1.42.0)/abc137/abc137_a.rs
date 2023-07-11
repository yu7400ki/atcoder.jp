use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        a: isize,
        b: isize,
    }

    let ans = (a + b).max(a - b).max(a * b);

    println!("{}", ans);
}
