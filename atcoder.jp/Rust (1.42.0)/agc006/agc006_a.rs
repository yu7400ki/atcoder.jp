use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        s: String,
        t: String,
    }

    if s == t {
        println!("{}", n);
        return;
    }

    for i in 1..=n {
        if s[n-i..] != t[..i] {
            println!("{}", 2 * n - i + 1);
            return;
        }
    }
}
