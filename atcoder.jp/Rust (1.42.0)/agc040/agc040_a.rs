use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        s: String,
    }

    let mut a = vec![0i64; s.len() + 1];

    for (i, c) in s.chars().enumerate() {
        match c {
            '<' => a[i + 1] = a[i] + 1,
            _ => (),
        }
    }

    a.reverse();

    for (i, c) in s.chars().rev().enumerate() {
        match c {
            '>' => a[i + 1] = a[i + 1].max(a[i] + 1),
            _ => (),
        }
    }

    let ans = a.iter().sum::<i64>();

    println!("{:?}", ans);
}
