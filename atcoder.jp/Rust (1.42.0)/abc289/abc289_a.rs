use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {
        s: Chars,
    }

    let s = s
        .into_iter()
        .map(|c| if c == '1' { '0' } else { '1' })
        .collect::<String>();

    println!("{}", s);
}
