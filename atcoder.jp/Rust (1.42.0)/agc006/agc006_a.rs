use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        s: String,
        t: String,
    }

    for i in 0..n {
        if s[i..] == t[..n - i] {
            println!("{}", n + i);
            return;
        }
    }

    println!("{}", 2 * n);
}
