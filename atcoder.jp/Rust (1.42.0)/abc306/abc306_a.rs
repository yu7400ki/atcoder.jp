use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {
        _n: usize,
        s: Chars,
    }

    let ans = s
        .into_iter()
        .map(|c| c.to_string().repeat(2))
        .collect::<Vec<_>>()
        .join("");

    println!("{}", ans);
}
