use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        s: String,
    }

    let mut ans = 0;

    for (i, c) in s.chars().enumerate() {
        match c {
            'U' => ans += s.len() - i - 1 + i * 2,
            'D' => ans += i + (s.len() - i - 1) * 2,
            _ => unreachable!(),
        }
    }

    println!("{}", ans);
}
