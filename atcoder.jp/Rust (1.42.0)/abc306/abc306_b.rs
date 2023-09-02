use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        a: [char; 64]
    }

    let s = a
        .into_iter()
        .rev()
        .map(|c| c.to_string())
        .collect::<Vec<_>>()
        .join("");

    let ans = u64::from_str_radix(&s, 2).unwrap();
    println!("{}", ans);
}
