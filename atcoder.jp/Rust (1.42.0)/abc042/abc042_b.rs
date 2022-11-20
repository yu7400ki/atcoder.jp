use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        _l: usize,
        mut s: [String; n],
    }

    s.sort();

    println!("{}", s.join(""));
}
