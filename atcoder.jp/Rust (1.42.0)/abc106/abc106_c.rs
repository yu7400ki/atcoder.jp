use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        s: String,
        k: usize,
    }

    let first_not_one = s.chars().enumerate().find(|(_, c)| *c != '1');
    match first_not_one {
        Some((i, c)) if i < k => println!("{}", c),
        _ => println!("1"),
    }
}
