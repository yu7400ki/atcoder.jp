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

    let s = s.chars().collect::<Vec<_>>();
    let t = t.chars().collect::<Vec<_>>();

    for i in 0..n {
        if s[n-i-1] != t[i] {
            println!("{}", 2 * n - i);
            return;
        }
    }
}
